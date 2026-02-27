## 列表模板

```json
{
    "type": "View",
    "props": {"width": 1388, "height": 640, "sceneColor": "#000000"},
    "compId": 2,
    "nodeParent": -1,
    "child": [
        {
            "type": "Sprite",
            "searchKey": "Sprite",
            "props": {},
            "compId": 3,
            "nodeParent": 2,
            "child": [
                {
                    "type": "Image",
                    "props": {
                        "y": 100, "x": 100,
                        "width": 700, "height": 1000,
                        "skin": "res/common/list_bg.png"
                    },
                    "compId": 4,
                    "nodeParent": 3
                },
                {
                    "type": "List",
                    "props": {
                        "y": 120, "x": 120,
                        "var": "lst_items",
                        "width": 660, "height": 960,
                        "spaceY": 10,
                        "repeatX": 1,
                        "repeatY": 1
                    },
                    "compId": 5,
                    "nodeParent": 3,
                    "child": [
                        {
                            "type": "UIView",
                            "source": "uilayer/模块/ListItem.scene",
                            "props": {
                                "name": "render",
                                "runtime": "script/uilayer/模块/ListItem.ts"
                            },
                            "compId": 6,
                            "nodeParent": 5
                        }
                    ]
                }
            ]
        }
    ]
}
```
