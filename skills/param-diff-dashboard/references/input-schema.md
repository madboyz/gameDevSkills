# 输入格式

## 顶层结构

```json
{
  "title": "参数调整前后对比",
  "subtitle": "旧值 vs 新值",
  "summary": [
    {
      "label": "参数峰值",
      "value": "3000",
      "subvalue": "旧值 2750 · +9%",
      "accent": "#f97316"
    }
  ],
  "series": {
    "labels": ["采样点1", "采样点2"],
    "lineCharts": [
      {
        "title": "主参数曲线",
        "description": "调整前 vs 调整后",
        "baselineLabel": "调整前",
        "candidateLabel": "调整后",
        "baseline": [10, 20],
        "candidate": [12, 25]
      }
    ],
    "barCharts": [
      {
        "title": "关键参数分组对比",
        "description": "按采样点展示旧值和新值",
        "baselineLabel": "旧值",
        "candidateLabel": "新值",
        "baseline": [100, 120],
        "candidate": [110, 140]
      }
    ]
  },
  "rows": [
    {
      "name": "参数项A",
      "baseline": 100,
      "candidate": 110,
      "delta": "+10",
      "note": "调整该参数以优化整体曲线"
    }
  ]
}
```

## 必填字段

- `title`
- `subtitle`
- `summary`
- `series.labels`
- `rows`

## 摘要卡片字段

| 字段 | 含义 |
| --- | --- |
| label | 卡片标题 |
| value | 主指标值 |
| subvalue | 对比文字 |
| accent | 可选文字颜色 |

## 行字段

| 字段 | 含义 |
| --- | --- |
| name | 主对比键 |
| baseline | 旧值 |
| candidate | 新值 |
| delta | 格式化差异文字 |
| note | 人工可读说明 |

## 图表规则

所有数据数组必须与 `series.labels` 对齐。若不需要某类图表，可传空数组 `lineCharts` 或 `barCharts`。

若报告用于 xlsx 参数调整，可把 `series.labels` 视为曲线横轴，如关卡索引、阶段索引、日期、采样点或参数分段。