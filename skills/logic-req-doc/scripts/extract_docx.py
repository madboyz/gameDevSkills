#!/usr/bin/env python3
"""从 .docx 策划文档提取纯文本（段落 + 表格），供逻辑需求文档生成使用。"""

import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def _text_from_element(elem: ET.Element) -> str:
    parts = []
    for t in elem.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"):
        if t.text:
            parts.append(t.text)
        if t.tail:
            parts.append(t.tail)
    return "".join(parts).strip()


def extract_docx(path: Path) -> str:
    lines: list[str] = []
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
        body = root.find("w:body", NS)
        if body is None:
            return ""

        for child in body:
            tag = child.tag.rsplit("}", 1)[-1]
            if tag == "p":
                text = _text_from_element(child)
                if text:
                    lines.append(text)
            elif tag == "tbl":
                lines.append("[表格]")
                for row in child.findall(".//w:tr", NS):
                    cells = []
                    for cell in row.findall(".//w:tc", NS):
                        cell_text = _text_from_element(cell)
                        cells.append(cell_text.replace("\n", " "))
                    if any(cells):
                        lines.append(" | ".join(cells))
                lines.append("[/表格]")

    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python extract_docx.py <docx路径>", file=sys.stderr)
        return 1

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"文件不存在: {path}", file=sys.stderr)
        return 1
    if path.suffix.lower() != ".docx":
        print("仅支持 .docx 文件", file=sys.stderr)
        return 1

    print(extract_docx(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
