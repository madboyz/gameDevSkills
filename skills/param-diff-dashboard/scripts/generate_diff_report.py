#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--template",
        default=str(Path(__file__).resolve().parent.parent / "assets" / "difficulty_curve_template.html"),
    )
    return parser.parse_args()


def validate_payload(data: dict) -> None:
    required = ["title", "subtitle", "summary", "series", "rows"]
    missing = [key for key in required if key not in data]
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")
    if "labels" not in data["series"]:
        raise ValueError("series.labels is required")
    data["series"].setdefault("lineCharts", [])
    data["series"].setdefault("barCharts", [])


def main() -> None:
    args = parse_args()
    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    validate_payload(payload)
    template = Path(args.template).read_text(encoding="utf-8")
    report = (
        template.replace("__REPORT_TITLE__", payload["title"])
        .replace("__REPORT_SUBTITLE__", payload["subtitle"])
        .replace("__REPORT_DATA__", json.dumps(payload, ensure_ascii=False))
    )
    Path(args.output).write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()
