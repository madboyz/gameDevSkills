# gameDevSkills

游戏开发所用到的 SKILL 集合。

---

## 分析结果概览

| 技能 | 主要作用 |
|------|----------|
| **ecs-logic-development** | ECS 框架下的游戏逻辑开发规范（组件、系统、数据中心、分层约束等） |
| **engine-debug** | Cocos Creator 引擎源码调试与问题定位（基于 `scripting/engine`） |
| **config-type-definition** | 根据 JSON 配置和源码定义 TypeScript 配置类型 |
| **source-code-reference** | 功能移植、实现与排查时优先参考源码（如 PuzzleBall 的 `game.js`） |
| **laya-debugging** | LayaAir 引擎调试（基于 `bin/libs`） |
| **skill-creator** | 创建、维护 Agent Skill 的流程与规范 |
| **refactor-func-click** | 将 Laya 点击事件重构为 `Func.AddClick` / `Func.RemoveClick` |
| **json-to-xlsx** | 将 JSON 配置批量转换为 XLSX 表格 |
| **laya-scene-generation** | 生成符合 LayaAir 规范的 `.scene` UI 配置文件 |

---

## 技能列表

| 技能名称 | 路径 | 作用说明 |
|---------|------|----------|
| **ecs-logic-development** | `skills/ecs-logic-development/` | 基于 ECS（Entity-Component-System）框架编写游戏逻辑的规范与最佳实践。涵盖 SOA 架构、组件/系统/数据中心命名、创建流程、API 使用、工厂模式、性能优化及 Framework/Logic 分层约束。 |
| **engine-debug** | `skills/engine-debug/` | Cocos Creator 引擎源码调试与问题定位指南。基于 `scripting/engine` 目录定位引擎相关问题，包含问题识别、源码定位、常见调试案例（Sprite 加载、资源释放、渲染异常）及引擎版本升级注意事项。 |
| **config-type-definition** | `skills/config-type-definition/` | 根据源码和配置 JSON 定义 TypeScript 配置数据类型。规范使用 `export type`、字段类型推断、可选字段规则，并指导在 ConfigRoot 中声明与加载配置。 |
| **source-code-reference** | `skills/source-code-reference/` | 功能移植、逻辑实现或问题排查时，优先参考源码确保实现准确一致。适用于 PuzzleBall 等项目，强调在 `game.js` 等源码中查找类、方法、数据结构，并正确转换为 TypeScript 类型。 |
| **laya-debugging** | `skills/laya-debugging/` | LayaAir 引擎源码调试与问题定位指南。基于 `bin/libs` 目录分析引擎行为，涵盖资源加载、UI 显示、内存泄漏等调试案例，以及 Chrome DevTools、Laya.Stat 等工具使用。 |
| **skill-creator** | `skills/skill-creator/` | 创建与维护 Agent Skill 的指南。包含技能结构（SKILL.md、scripts、references、assets）、渐进式披露设计、创建流程（理解需求 → 规划资源 → 初始化 → 编辑 → 打包 → 迭代），以及 init_skill.py、package_skill.py 等脚本用法。 |
| **refactor-func-click** | `skills/refactor-func-click/` | 自动化重构 LayaAir TypeScript 文件，使其符合 `require-func-click` ESLint 规则。将 `Laya.Event.CLICK` / `MouseEvent.CLICK` 的 `.on` / `.once` / `.off` 替换为 `Func.AddClick` / `Func.RemoveClick`。 |
| **json-to-xlsx** | `skills/json-to-xlsx/` | 将 JSON 配置文件批量转换为 XLSX 表格。支持 4 行表头（显示名、类型、字段名、格式提示），扁平化嵌套对象、序列化数组，需用户指定 JSON 目录路径。 |
| **laya-scene-generation** | `skills/laya-scene-generation/` | 根据需求生成符合 LayaAir 规范的 `.scene` UI 配置文件。支持 View、Image、Button、List 等组件，需参考图与资源路径，遵循 compId、nodeParent、命名等规范，不写入 Script 组件。 |

---

## 按场景分类

### 引擎与框架
- **ecs-logic-development**：ECS 逻辑开发
- **engine-debug**：Cocos Creator 调试
- **laya-debugging**：LayaAir 调试

### 配置与数据
- **config-type-definition**：配置类型定义
- **json-to-xlsx**：JSON 转 Excel

### 代码与工具
- **source-code-reference**：源码参考优先
- **refactor-func-click**：点击事件重构
- **laya-scene-generation**：Laya 场景生成

### 技能管理
- **skill-creator**：创建与管理技能
