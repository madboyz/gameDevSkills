---
name: param-diff-dashboard
description: Generate a local parameter-diff dashboard for before-after data changes. Use when Claude needs to turn adjusted xlsx parameters or other structured document data into a reviewable HTML report with KPI cards, charts, and detailed diff tables, especially for showing parameter curves, trend changes, and old-vs-new comparisons.
---

# 参数对比仪表盘

## 概述

将结构化前后数据转换为本地 HTML 报告，评审者可直接在浏览器打开。适用于修改 xlsx 或其他结构化源后的通用参数对比，方便查看新旧值、曲线变化、指标差异及行级详情。`artifact/difficulty_curve.html` 仅作为深色仪表盘布局的视觉参考，不限制业务场景。

## 输入

准备一份 JSON，包含：

- `title`
- `subtitle`
- `summary`
- `series`
- `rows`

详见 `references/input-schema.md` 中的格式与最小示例。

## 工作流

1. 将源数据归一化为一份前后对比 JSON。
2. 选定主对比维度，如参数步长、阶段、关卡、工作表行、日期桶或需求 ID。
3. 选最多三项核心指标作为 KPI 卡片，至少一条主曲线或趋势序列。
4. 渲染 HTML 报告。
5. 本地打开，确认图表与表格内容。

## 视觉规则

- 标题简短，突出结果。
- 第一张摘要卡片展示最重要的增量。
- 旧值用低饱和色，新值用暖色高亮。
- 曲线、进度、趋势对比用折线图；分组对比用柱状图。
- 明细表即使非交互，也需让人可手动排序。

## 模板指引

`assets/difficulty_curve_template.html` 复刻了既有 artifact 的布局语言，但未硬编码具体业务数据。需要快速生成深色主题的 xlsx 参数调整、新旧曲线或其他结构化 diff 评审时，可直接复用。

## 辅助脚本

```bash
python scripts/generate_diff_report.py --input report-data.json --output diff-report.html
```

脚本会填充自带模板并输出独立 HTML。默认通过 CDN 加载 Chart.js；若需离线，把生成文件里的脚本地址换成本地副本即可。

## 报告设计要点

- `rows` 主键在前后版本保持一致。
- 数值图表数据放入 `series`。
- 每行用 `note` 字段存放理由或说明。
- 针对表格变更，每行对应一个业务实体、参数项或采样点，而非原始单元格。
- 若主要目标是观察曲线变化，确保 `series.labels` 在调整前后代表同一横轴。

## 与其他技能协作

- 对比数据筛选前，用 `qmd-doc-context` 对源目录做清点与摘要。
- 若调整后的数值仍需深度推理，再用 `hybrid-cloud-revision` 定稿，最后发布报告。

## 参考

- 阅读 `references/input-schema.md` 以正确准备 JSON 输入。