## 弹窗模板

```json
{
    "type": "View",
    "props": {"width": 1388, "height": 640, "sceneColor": "#000000"},
    "compId": 2,
    "nodeParent": -1,
    "child": [
        {
            "type": "Box",
            "searchKey": "Box",
            "props": {"width": 1388, "height": 640},
            "compId": 3,
            "nodeParent": 2,
            "child": []
        },
        {
            "type": "Sprite",
            "searchKey": "Sprite",
            "props": {"y": 320, "x": 694},
            "compId": 4,
            "nodeParent": 2,
            "child": [
                {
                    "type": "Image",
                    "props": {
                        "y": 0, "x": 0,
                        "skin": "res/oldpic/confirm/yt_panel_10.png",
                        "anchorX": 0.5, "anchorY": 0.5
                    },
                    "compId": 5,
                    "nodeParent": 4
                },
                {
                    "type": "Image",
                    "props": {
                        "y": -200, "x": 0,
                        "skin": "res/oldpic/confirm/yt_titlebg_04.png",
                        "anchorX": 0.5, "anchorY": 0.5
                    },
                    "compId": 6,
                    "nodeParent": 4
                },
                {
                    "type": "Button",
                    "props": {
                        "y": -200, "x": 300,
                        "var": "btn_close",
                        "stateNum": "1",
                        "skin": "res/oldpic/confirm/yt_btn_close.png",
                        "anchorX": 0.5, "anchorY": 0.5
                    },
                    "compId": 7,
                    "nodeParent": 4
                },
                {
                    "type": "Panel",
                    "props": {
                        "y": -100, "x": 0,
                        "var": "pn_content",
                        "width": 600, "height": 300,
                        "anchorX": 0.5
                    },
                    "compId": 8,
                    "nodeParent": 4,
                    "child": [
                        {
                            "type": "Label",
                            "searchKey": "Label",
                            "props": {
                                "y": 0, "x": 0,
                                "text": "内容文本",
                                "fontSize": 36,
                                "color": "#575047",
                                "align": "center",
                                "wordWrap": true,
                                "width": 600
                            },
                            "compId": 9,
                            "nodeParent": 8
                        }
                    ]
                },
                {
                    "type": "Button",
                    "props": {
                        "y": 180, "x": -100,
                        "var": "btn_cancel",
                        "stateNum": "1",
                        "skin": "res/public/btn_mid2.png",
                        "label": "取消",
                        "labelSize": 30,
                        "labelColors": "#20545e,#20545e,#20545e"
                    },
                    "compId": 10,
                    "nodeParent": 4
                },
                {
                    "type": "Button",
                    "props": {
                        "y": 180, "x": 100,
                        "var": "btn_confirm",
                        "stateNum": "1",
                        "skin": "res/public/btn_mid1.png",
                        "label": "确定",
                        "labelSize": 30,
                        "labelColors": "#ac7434,#ac7434,#ac7434"
                    },
                    "compId": 11,
                    "nodeParent": 4
                }
            ]
        }
    ]
}
```
