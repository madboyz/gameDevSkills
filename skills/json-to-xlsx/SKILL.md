---
name: json-to-xlsx
description: Convert JSON config files to XLSX spreadsheets with 4-row headers (display name, type, field name, format hint). Requires user to specify the JSON directory path. Use when the user needs to export JSON configs to Excel or generate XLSX from game config data.
---

# JSON Config to XLSX Converter

## Overview

Convert JSON config files to XLSX format following the project's 4-row header convention observed in `excel/` reference files.

**需用户指定要转换的 JSON 目录路径**，直接作为第一个参数传入。

## Prerequisites

```bash
pip install openpyxl
```

## Quick Start

转换指定目录下所有 JSON（直接传入目录路径）：

```bash
python .cursor/skills/json-to-xlsx/scripts/json_to_xlsx.py <JSON目录路径>
```

示例（puzzleball 配置）：

```bash
python .cursor/skills/json-to-xlsx/scripts/json_to_xlsx.py bin/res/puzzleball/config/
```

仅转换部分文件：

```bash
python .cursor/skills/json-to-xlsx/scripts/json_to_xlsx.py <JSON目录路径> -f roleSkill dayTask stageReward
```

指定输出目录：

```bash
python .cursor/skills/json-to-xlsx/scripts/json_to_xlsx.py <JSON目录路径> -o output/xlsx/
```

## XLSX Structure (4-Row Header)

| Row | Content | Example |
|-----|---------|---------|
| 0 | Display name | `id`, `name`, `complete_id` |
| 1 | Type declaration | `INT`, `STRING`, `FLOAT` |
| 2 | Field name | `id`, `name`, `complete_id` |
| 3 | Format hint | `INT`, `STRING`, `[_]`, `[,_]` |
| 4+ | Data rows | Actual values |

## Data Handling Rules

1. **Flat values** (`"id": 1`, `"name": "text"`) map directly to columns
2. **Nested objects** (`"complete": {"id": 1, "num": 1}`) flatten to `complete_id`, `complete_num`
3. **Arrays** (`[10, 13, 17]`) serialize with `_` separator: `"10_13_17"`
4. **String values** are kept as-is without modification

## Verification

Read back generated XLSX:

```bash
python .cursor/skills/json-to-xlsx/scripts/read_xlsx.py output.xlsx
python .cursor/skills/json-to-xlsx/scripts/read_xlsx.py output.xlsx --headers-only
python .cursor/skills/json-to-xlsx/scripts/read_xlsx.py output.xlsx -n 5
```

## Script Parameters

### json_to_xlsx.py

| Param | Short | Description |
|-------|-------|-------------|
| `input_dir` | | **必填**，位置参数，用户指定的 JSON 文件所在目录路径 |
| `--output-dir` | `-o` | XLSX output directory (default: `<input-dir>/../xlsx/`) |
| `--files` | `-f` | Specific JSON filenames to convert |

### read_xlsx.py

| Param | Short | Description |
|-------|-------|-------------|
| `xlsx_path` | | XLSX file path (positional, required) |
| `--sheet` | `-s` | Sheet name (default: active) |
| `--max-rows` | `-n` | Max data rows to read |
| `--headers-only` | | Only print header info |
| `--output` | `-o` | Output JSON file path |
