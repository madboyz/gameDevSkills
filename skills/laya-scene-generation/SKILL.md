---
name: Laya Scene 文件生成
description: 根据需求生成符合 LayaAir 规范的 .scene UI 配置文件
---

# Laya Scene 文件生成 Skill

## 能力说明

此 Skill 用于根据用户需求生成符合 LayaAir 引擎规范的 `.scene` UI 配置文件。可以创建完整的界面布局，包括各种 UI 组件、样式配置、层级结构等。

## 基础规则说明

- **参考图必需**: 必须要求用户提供参考图，根据参考图进行 UI 布局和组件生成
- **文件位置**: UI 文件必须存放在 `laya/pages/uilayer/` 目录下
- **模块文件夹**: 如果目标模块文件夹不存在，必须先询问用户指定文件夹名称才能创建，否则不执行创建操作
- **脚本资源**: 所有组件中用到的脚本资源（Script 组件），不要写入到生成的 scene 文件中
- **组件 ID**: 每个组件的 `compId` 从 2 开始递增，在同一个 scene 文件中不能重复
- **根节点固定**: 根节点的 `compId` 始终为 2，`nodeParent` 为 -1
- **根节点大小**: 根节点 `View` 的 `width` 和 `height` 必须严格按照效果图的实际像素尺寸设置，默认为 1388 * 640
- **资源路径必需**: 必须要求用户输入资源路径
- **指定资源使用**: 如用户对背景图、按钮等指定了资源名，生成时必须将其写入到 scene 文件中
- **背景图处理**: 如用户指定背景图，需在 View 下的子节点创建一个 Image 组件的节点，同时将 `skin` 设置为指定背景图路径
- **按钮处理**: 如用户没有指定按钮多态，默认设置 `stateNum` = 1
- **List组件使用**: 效果图中如出现多个同样的按钮、图片框等重复元素，必须使用 List 组件，并生成对应的 Item scene 文件（命名格式：`xxxxItem.scene`）

## 文件格式规范

### 基本结构

```json
{
    "x": 0,
    "type": "View",
    "selectedBox": <最后选中的节点ID>,
    "selecteID": <最后选中的节点ID>,
    "searchKey": "View",
    "props": {
        "width": <宽度>,
        "height": <高度>,
        "sceneColor": "<背景颜色>",
        "sceneBg": "<可选：背景图路径>",
        "mouseThrough": false
    },
    "nodeParent": -1,
    "maxID": <最大ID值>,
    "label": "View",
    "isOpen": true,
    "isDirectory": true,
    "isAniNode": true,
    "hasChild": true,
    "compId": 2,
    "child": [<子节点数组>],
    "animations": [
        {
            "nodes": [],
            "name": "ani1",
            "id": 1,
            "frameRate": 24,
            "action": 0
        }
    ],
    "$HIDDEN": false
}
```

### 节点通用属性

每个节点必须包含以下属性：

```json
{
    "type": "组件类型",
    "searchKey": "组件类型,变量名",
    "props": {<组件特定属性>},
    "nodeParent": <父节点compId>,
    "label": "节点标签",
    "isDirectory": <是否是容器>,
    "isAniNode": true,
    "hasChild": <是否有子节点>,
    "compId": <唯一ID>,
    "child": [<子节点>]
}
```

## 组件类型详解

详细组件类型说明请参考: [组件类型详解](references/components.md)

## 颜色码规范

详细颜色码规范请参考: [颜色码规范](references/colors.md)

## 布局定位规范

### 绝对定位
```json
{
    "x": 100,
    "y": 200
}
```

### 居中定位
```json
{
    "centerX": 0,    // 水平居中，0 表示容器中心
    "centerY": 0,    // 垂直居中
    "anchorX": 0.5,
    "anchorY": 0.5
}
```

### 常用锚点组合
```json
// 左上角（默认）
{"anchorX": 0, "anchorY": 0}

// 中心点
{"anchorX": 0.5, "anchorY": 0.5}

// 右上角
{"anchorX": 1, "anchorY": 0}

// 右下角
{"anchorX": 1, "anchorY": 1}
```

## 资源路径规范

### 图片资源
- 位置: `res/` 目录
- 示例: `"res/oldpic/confirm/yt_panel_10.png"`

### 引用路径规则 (source/runtime)

#### 1. 脚本引用
- **适用情况**: 当 `source` 或 `runtime` 引用脚本文件时
- **基准目录**: `e:\Project\baizhan_slg\baizhan_pro\china\code\client\src`
- **格式**: 必须以 `src/` 开头
- **示例**: `"src/script/plugins/PlugAnchor.ts"`

#### 2. 场景引用
- **适用情况**: 当 `source` 引用其他 `.scene` 文件时（如 UIView 组件）
- **基准目录**: `e:\Project\baizhan_slg\baizhan_pro\china\code\client\laya\pages`
- **格式**: 相对于 `pages` 目录的路径
- **示例**: `"uilayer/meirirenwu/xitongyugaoitem.scene"`

## 命名与变量规范

详细命名与变量规范请参考: [命名与变量规范](references/naming.md)


## 典型UI模式模板

详细模板请参考:
- [弹窗模板](references/templates/dialog.md)
- [列表模板](references/templates/list.md)


## 使用流程

### 步骤 1: 确认需求
询问用户以下信息：
1. UI 的用途和功能
2. 目标模块名称（文件夹名）
3. 场景尺寸（默认 1388x640）
4. UI 类型（弹窗、列表、标签页等）

### 步骤 2: 检查模块文件夹
检查 `laya/pages/uilayer/模块名/` 是否存在，如果不存在则询问用户确认创建。

### 步骤 3: 生成 scene 文件
1. 根据需求确定组件层级结构
2. 分配 compId（从 2 开始递增）
3. 设置 nodeParent 关系
4. 配置组件属性和样式
5. **不要添加 Script 组件**

### 步骤 4: 保存文件
将生成的 JSON 保存到：
```
laya/pages/uilayer/模块名/ViewXxx.scene
```

## 注意事项

1. **compId 管理**: 必须从 2 开始，根节点固定为 2
2. **nodeParent 关系**: 确保所有节点正确指向父节点的 compId
3. **maxID 更新**: 设置为所有 compId 中的最大值
4. **不含脚本**: 生成的 scene 文件中不要包含 Script 类型组件
5. **路径规范**: 所有资源路径使用相对路径
6. **颜色格式**: 使用十六进制颜色码，如 `#ffffff`
7. **九宫格**: sizeGrid 格式为 `"上,右,下,左"`

## 常见错误避免

❌ **错误示例**:
```json
// compId 从 1 开始
{"compId": 1, "nodeParent": -1}

// nodeParent 指向不存在的节点
{"compId": 5, "nodeParent": 99}

// 包含了 Script 组件
{
    "type": "Script",
    "source": "src/script/plugins/PlugAnchor.ts"
}
```

✅ **正确示例**:
```json
// compId 从 2 开始
{"compId": 2, "nodeParent": -1}

// nodeParent 正确指向
{"compId": 5, "nodeParent": 2}

// 不包含 Script 组件
{
    "type": "Sprite",
    "searchKey": "Sprite",
    "props": {}
}
```

## 完整示例

参考 `laya/pages/uilayer/common/Confirm.scene` 作为标准弹窗示例。

参考 `laya/pages/uilayer/chat/ViewChat.scene` 作为复杂界面示例。

## 对话提示词 参考
使用技能此技能
#SKILL.md 参考效果图，创建一个文件夹qianlong1，界面命名为ViewQianLongMain，创建界面 scene文件 ,资源路径为 #qianlong1 ,背景图使用 #qlzb_01.jpg
