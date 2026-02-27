## 命名规范

### 变量名（var）前缀

**重要约束**: 只有以下列出的组件类型需要设置 `var` 变量名，其他所有组件类型都不应设置变量名，必须遵守"不设置变量名的组件示例"与 "不设置变量名的组件类型"规则。

```
btn_    - 按钮（Button）
pn_     - 面板（Panel）
lst_    - 列表（List）
tf_     - 字体剪辑（FontClip）

```

### 文件命名
```
ViewXxx.scene      - 主视图
XxxItem.scene      - 列表项
XxxPanel.scene     - 子面板
XxxTab.scene       - 标签页
```

## 组件变量命名规则

### 必须设置变量名的组件类型
以下组件类型**必须**设置 `var` 变量名：
- **Button**（按钮）
- **List**（列表）
- **FontClip**（位图字体）
- **Panel**（面板）

### 不设置变量名的组件类型
以下组件类型**不应**设置 `var` 变量名：
- **Box**（盒子容器）
- **Image**（图像）
- **Label**（标签）
- **Text**（文本）

## 组件变量属性规则

### 设置变量名的组件示例

**Button 示例**:
```json
{
    "type": "Button",
    "searchKey": "Button,btn_confirm",
    "props": {
        "var": "btn_confirm",
        "skin": "res/public/btn_mid1.png"
    }
}
```

**List 示例**:
```json
{
    "type": "List",
    "searchKey": "List,lst_items",
    "props": {
        "var": "lst_items",
        "width": 500,
        "height": 600
    }
}
```

**Panel 示例**:
```json
{
    "type": "Panel",
    "searchKey": "Panel,pn_content",
    "props": {
        "var": "pn_content",
        "width": 500,
        "height": 400
    }
}
```

**FontClip 示例**:
```json
{
    "type": "FontClip",
    "searchKey": "FontClip,tf_num",
    "props": {
        "var": "tf_num",
        "value": "12345",
        "skin": "res/public/img_zlnumxiao.png",
        "sheet": "0123456789"
    }
}
```

### 不设置变量名的组件示例

**Box 示例**:
```json
{
    "type": "Box",
    "searchKey": "Box",
    "props": {
        "x": 0,
        "y": 0,
        "width": 500,
        "height": 300
    }
}
```

**Image 示例**:
```json
{
    "type": "Image",
    "searchKey": "Image",
    "props": {
        "x": 0,
        "y": 0,
        "skin": "res/common/bg.png"
    }
}
```

**Label 示例**:
```json
{
    "type": "Label",
    "searchKey": "Label",
    "props": {
        "x": 0,
        "y": 0,
        "text": "标题",
        "fontSize": 24,
        "color": "#ffffff"
    }
}
```

**Text 示例**:
```json
{
    "type": "Text",
    "searchKey": "Text",
    "props": {
        "x": 0,
        "y": 0,
        "text": "文本内容",
        "fontSize": 20
    }
}
```
