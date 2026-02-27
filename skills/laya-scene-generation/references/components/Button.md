## Button（按钮）

可点击交互按钮。

**常用属性**:
```json
{
    "type": "Button",
    "props": {
        "x": 0,
        "y": 0,
        "var": "btn_confirm",
        "stateNum": "1",
        "skin": "res/public/btn_mid1.png",
        "label": "确定",
        "labelSize": 30,
        "labelColors": "#ac7434,#ac7434,#ac7434",
        "labelStroke": 1,
        "labelStrokeColor": "#353535",
        "anchorX": 0.5,
        "anchorY": 0.5
    }
}
```

**stateNum 说明**:
- `"1"`: 单态（仅一种显示状态）
- `"2"`: 双态（正常、按下）
- `"3"`: 三态（正常、悬停、按下）
