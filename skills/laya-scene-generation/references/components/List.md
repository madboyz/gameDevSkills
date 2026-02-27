## List（列表）

列表容器，支持虚拟滚动。

**常用属性**:
```json
{
    "type": "List",
    "props": {
        "x": 0,
        "y": 0,
        "var": "lst_items",
        "width": 500,
        "height": 600,
        "spaceX": 10,
        "spaceY": 10,
        "repeatX": 1,
        "repeatY": 1,
        "vScrollBarSkin": "res/ui/vscroll.png"
    },
    "child": [
        {
            "type": "UIView",
            "source": "uilayer/模块/ItemTemplate.scene",
            "props": {
                "name": "render",
                "runtime": "script/uilayer/模块/ItemTemplate.ts"
            }
        }
    ]
}
```
