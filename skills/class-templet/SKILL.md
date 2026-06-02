---
name: class-templet
description: 快速创建符合项目规范的 UI 界面和组件类模板。支持创建普通全屏/半屏界面 (UILayer)、弹窗 (UITips) 和独立组件 (Component)。当用户请求创建新的 UI 类、界面、弹窗或 Item 组件时，使用此技能生成符合命名规范、目录结构和继承关系的 TypeScript 代码。
---

# UI 类模板技能 (class-templet)

本技能通过预定义的代码模板，帮助 Agent 快速生成符合项目规范的 UI 界面和组件代码，确保代码一致性。

## 核心流程

### 1. 识别 UI 类型 (Selection Guidance)

根据用户需求选择最合适的模板：

- **普通界面 (UILayer)**：全屏、半屏或功能主界面（如 `Mail`, `Shop`, `Bag`）。继承自 `UILayer`。
- **弹窗/提示 (UITips)**：二次确认框、奖励获得、简单提示（如 `MailTips`, `ConfirmTips`）。继承自 `UITips`。
- **独立组件 (Component)**：列表项、页签、公共单元（如 `MailItem`, `TabBtn`）。继承自 `fgui.GComponent`。

### 2. 推导命名参数

| 参数名 | 规则 | 示例 (以 Mail 为例) |
| :--- | :--- | :--- |
| **PkgName** | 全小写 (FGUI 包名) | `mail` |
| **ClassName** | 大驼峰 (PascalCase) | `Mail` (UILayer), `MailTips` (UITips), `MailItem` (Comp) |
| **CompName** | 大驼峰 (FGUI 组件名) | `Mail`, `MailTips`, `MailItem` |
| **uipara 类型** | `PkgName_CompName` | `mail_Mail`, `mail_MailTips`, `mail_MailItem` |

### 3. 生成与放置

1.  **读取模板**：从 `references/` 目录读取对应的 `.md` 文件。
2.  **替换占位符**：将模板中的 `ClassName`, `PkgName`, `CompName`, `PkgName_CompName` 替换为推导出的实际值。
3.  **确定路径**：统一放置在 `assets/scripts/logic/uilayer/` 下的对应业务子目录中。
    - 例如：`assets/scripts/logic/uilayer/mail/Mail.ts`
4.  **写入文件**：生成完整的 TypeScript 代码。

## 规范与约束

- **命名规范**：遵循 `base-proj-rules.md`，类名和文件名必须一致且使用大驼峰。
- **FGUI 导入**：统一使用 `import * as fgui from 'fairygui-cc'`。
- **路径别名**：优先使用 `@logic/*`, `@framework/*`, `@gamestart/*`。
- **分层限制**：UI 代码属于 Logic 层，禁止引用 Framework 层以外的底层实现（除非通过 Manager）。

## 模板参考

- [UILayer 模板](references/UILayerTemplet.md)
- [UITips 模板](references/UITipsTemplet.md)
- [Component 模板](references/ComponentTemplet.md)
