# gameDevSkills

游戏开发所用的 **Skills** 与 **Rules** 集合。

- **Skills**（`skills/`）：17 个专项技能，提供特定任务的工作流与脚本
- **Rules**（`rules/`）：7 条 Agent 规则，定义项目约束与协作规范

---

## Skills 分析结果概览

| 技能 | 主要作用 |
|------|----------|
| **ecs-logic-development** | ECS 框架下的游戏逻辑开发规范（组件、系统、数据中心、分层约束等） |
| **engine-debug** | Cocos Creator 引擎源码调试与问题定位（基于 `scripting/engine`） |
| **laya-debugging** | LayaAir 引擎源码调试与问题定位（基于 `bin/libs`） |
| **config-type-definition** | 根据 JSON 配置和源码定义 TypeScript 配置类型 |
| **json-to-xlsx** | 将 JSON 配置批量转换为 XLSX 表格 |
| **puzzleball-config-doc** | 根据 game.js 分析 PuzzleBall JSON 配置的用途与使用逻辑，生成说明文档 |
| **param-diff-dashboard** | 将参数调整前后数据生成本地 HTML 对比仪表盘（KPI、图表、明细表） |
| **source-code-reference** | 功能移植、实现与排查时优先参考源码（如 PuzzleBall 的 `game.js`） |
| **refactor-func-click** | 将 Laya 点击事件重构为 `Func.AddClick` / `Func.RemoveClick` |
| **karpathy-guidelines** | LLM 编码行为准则，避免过度设计、做最小改动、明确假设与验收标准 |
| **class-templet** | 快速创建符合项目规范的 UI 界面、弹窗、组件 TypeScript 类模板 |
| **laya-scene-generation** | 生成符合 LayaAir 规范的 `.scene` UI 配置文件 |
| **atlas-packer** | 将小图 `.jpg` 拼合为 `.png` 图集，并生成 `atlas_map.json` 映射 |
| **logic-req-doc** | 根据策划 docx、配置表、协议生成前后端职责清晰的逻辑需求文档 |
| **dev-plan-tracker** | 维护开发计划与交接记录，按模块写入 `doc/plan/` |
| **hybrid-cloud-revision** | 本地上下文 + 云端推理的混合文档修订（xlsx、docx、md 等） |
| **skill-creator** | 创建、维护 Agent Skill 的流程与规范 |

---

## Skills 技能列表

| 技能名称 | 路径 | 作用说明 |
|---------|------|----------|
| **ecs-logic-development** | `skills/ecs-logic-development/` | 基于 ECS（Entity-Component-System）框架编写游戏逻辑的规范与最佳实践。涵盖 SOA 架构、组件/系统/数据中心命名、创建流程、API 使用、工厂模式、性能优化及 Framework/Logic 分层约束。 |
| **engine-debug** | `skills/engine-debug/` | Cocos Creator 引擎源码调试与问题定位指南。业务异常须先在 `scripting/engine` 中归因根因，再给出业务/框架层修改建议。包含问题识别、源码定位、常见调试案例及引擎版本升级注意事项。 |
| **laya-debugging** | `skills/laya-debugging/` | LayaAir 引擎源码调试与问题定位指南。基于 `bin/libs` 目录分析引擎行为，涵盖资源加载、UI 显示、内存泄漏等调试案例，以及 Chrome DevTools、Laya.Stat 等工具使用。 |
| **config-type-definition** | `skills/config-type-definition/` | 根据源码和配置 JSON 定义 TypeScript 配置数据类型。规范使用 `export type`、字段类型推断、可选字段规则，并指导在 ConfigRoot 中声明与加载配置。 |
| **json-to-xlsx** | `skills/json-to-xlsx/` | 将 JSON 配置文件批量转换为 XLSX 表格。支持 4 行表头（显示名、类型、字段名、格式提示），扁平化嵌套对象、序列化数组，需用户指定 JSON 目录路径。 |
| **puzzleball-config-doc** | `skills/puzzleball-config-doc/` | 根据 game.js 源码分析 `bin/res/puzzleball/config` 中指定 JSON 配置的用途与使用逻辑，并生成说明文档。必须由用户指定要分析的 JSON 配置文件名（如 boxShop.json、stageA.json）。 |
| **param-diff-dashboard** | `skills/param-diff-dashboard/` | 将 xlsx 或其他结构化数据的参数调整前后对比，生成本地 HTML 评审报告。包含 KPI 卡片、趋势曲线、柱状图和明细 diff 表，便于查看新旧值与参数曲线变化。 |
| **source-code-reference** | `skills/source-code-reference/` | 功能移植、逻辑实现或问题排查时，优先参考源码确保实现准确一致。适用于 PuzzleBall 等项目，强调在 `game.js` 等源码中查找类、方法、数据结构，并正确转换为 TypeScript 类型。 |
| **refactor-func-click** | `skills/refactor-func-click/` | 自动化重构 LayaAir TypeScript 文件，使其符合 `require-func-click` ESLint 规则。将 `Laya.Event.CLICK` / `MouseEvent.CLICK` 的 `.on` / `.once` / `.off` 替换为 `Func.AddClick` / `Func.RemoveClick`。 |
| **karpathy-guidelines** | `skills/karpathy-guidelines/` | 减少 LLM 常见编码失误的行为准则。编写、审查或重构代码时使用：先明确假设、保持简单、做最小改动、只清理自己引入的冗余，并定义可验证的验收标准。 |
| **class-templet** | `skills/class-templet/` | 快速创建符合项目规范的 UI 类模板。支持 UILayer 全屏/半屏界面、UITips 弹窗、Component 列表项/页签等，自动生成命名、目录结构和继承关系正确的 TypeScript 代码。 |
| **laya-scene-generation** | `skills/laya-scene-generation/` | 根据需求生成符合 LayaAir 规范的 `.scene` UI 配置文件。支持 View、Image、Button、List 等组件，需参考图与资源路径，遵循 compId、nodeParent、命名等规范，不写入 Script 组件。 |
| **atlas-packer** | `skills/atlas-packer/` | 将目录下的小 `.jpg` 图块按 shelf 算法拼合为一个或多个 `.png` 图集，并生成 `atlas_map.json` 记录文件名与坐标映射。支持自定义最大尺寸（推荐 2048）。 |
| **logic-req-doc** | `skills/logic-req-doc/` | 根据策划 `.docx`、配置表（AllFilenamePara.d.ts / tb.d.tstype）、参考代码与 netdata 协议（PB*.ts / *.proto），生成含读表伪逻辑、协议时序、前后端职责划分的详细逻辑需求文档。 |
| **dev-plan-tracker** | `skills/dev-plan-tracker/` | 维护本项目开发计划与交接记录。修改代码、实现功能、修复 bug 或重构时，按主修改模块在 `doc/plan/` 下新建计划文件，记录目标、已完成、缺失、验证结果和后续入口。 |
| **hybrid-cloud-revision** | `skills/hybrid-cloud-revision/` | 本地-云端混合文档修订。本地完成索引与摘要后，将最小必要数据包发送云端进行跨文件一致性修订、政策/业务措辞改写或最终定稿，再回写本地并复核。 |
| **skill-creator** | `skills/skill-creator/` | 创建与维护 Agent Skill 的指南。包含技能结构（SKILL.md、scripts、references、assets）、渐进式披露设计、创建流程（理解需求 → 规划资源 → 初始化 → 编辑 → 打包 → 迭代），以及 init_skill.py、package_skill.py 等脚本用法。 |

---

## Skills 按场景分类

### 引擎与框架
- **ecs-logic-development**：ECS 逻辑开发
- **engine-debug**：Cocos Creator 调试
- **laya-debugging**：LayaAir 调试

### 配置与数据
- **config-type-definition**：配置类型定义
- **json-to-xlsx**：JSON 转 Excel
- **puzzleball-config-doc**：PuzzleBall 配置说明文档
- **param-diff-dashboard**：参数对比 HTML 仪表盘

### UI 与界面
- **class-templet**：UI 类模板生成
- **laya-scene-generation**：Laya 场景文件生成
- **atlas-packer**：图集打包

### 代码与开发
- **source-code-reference**：源码参考优先
- **refactor-func-click**：点击事件重构
- **karpathy-guidelines**：编码行为准则

### 文档与计划
- **logic-req-doc**：逻辑需求文档生成
- **dev-plan-tracker**：开发计划与交接记录
- **hybrid-cloud-revision**：本地-云端混合文档修订

### 技能管理
- **skill-creator**：创建与管理技能

---

## Rules 分析结果概览

| 规则 | 主要作用 |
|------|----------|
| **base-proj-rules** | 项目目录结构、代码分层、命名规范、ECS 与 FGUI 导入约定 |
| **typescript-rules** | TypeScript 命名、类型安全、产物体积与异步写法补充规范 |
| **fgui-rules** | FairyGUI 开发规则，以 `fairygui.mjs` 与项目 Demo 为准 |
| **doc-maintenance-rules** | 文档与代码同步维护，提交前文档自检 |
| **karpathy-guidelines** | LLM 编码行为准则（先思考、保持简单、最小改动、目标驱动） |
| **codegraph** | CodeGraph MCP 工具选用指南（结构查询优先于 grep） |
| **language** | 与用户交互、代码注释统一使用简体中文 |

---

## Rules 规则列表

| 规则名称 | 路径 | 生效范围 | 作用说明 |
|---------|------|----------|----------|
| **base-proj-rules** | `rules/base-proj-rules.md` | 始终生效 | 定义 `framework/` / `logic/` / `gamestart/` 分层职责与引用约束；文件夹小写、TS 大驼峰命名；ECS 组件/系统命名与 `@ecs.ECSClass` 修饰；FGUI 须 `import * as fgui from 'fairygui-cc'`；基于 Cocos Creator 3.8.8。 |
| **typescript-rules** | `rules/typescript-rules.md` | 始终生效 | 补充 TypeScript 命名（类/接口/方法/属性/常量）、类型安全、产物体积控制与 async/await 写法，与 `base-proj-rules.md` 一并遵守。 |
| **fgui-rules** | `rules/fgui-rules.md` | `uilayer/`、`uipara/`、`fgui/` 下 TS 文件 | FairyGUI 须以 `fairygui.mjs` 与项目内 Demo 为准，禁止臆测 API；虚拟列表接入顺序、Cocos 3.x 资源接口对齐。 |
| **doc-maintenance-rules** | `rules/doc-maintenance-rules.md` | 始终生效 | 代码与文档同源；架构/流程变更同步更新 `doc/`；接口变更更新 `doc/Standards/`；提交前检查废弃路径、全局变量、配置项等是否已在文档中反映。 |
| **karpathy-guidelines** | `rules/karpathy-guidelines.md` | 始终生效 | 减少 LLM 编码失误：先明确假设、保持简单、只做必要改动、定义可验证验收标准；与同名 skill 内容一致。 |
| **codegraph** | `rules/codegraph.mdc` | 始终生效 | CodeGraph MCP 使用指南。结构类问题（定义在哪、谁调用谁、影响范围）优先用 `codegraph_*` 工具；字面文本搜索仍用 grep/read。 |
| **language** | `rules/language.md` | 始终生效 | 所有对话、解释、代码注释使用简体中文；技术术语可保留英文，但说明须用中文。 |

---

## Rules 按场景分类

### 项目结构与编码
- **base-proj-rules**：目录分层、命名、ECS、FGUI 导入
- **typescript-rules**：TypeScript 编码补充规范

### UI 开发
- **fgui-rules**：FairyGUI API 与虚拟列表用法

### 文档与协作
- **doc-maintenance-rules**：文档同步与提交前自检
- **language**：中文交互与注释

### Agent 行为与工具
- **karpathy-guidelines**：编码行为准则
- **codegraph**：代码结构查询工具选用

---

## Skills 与 Rules 的关系

| 类型 | 定位 |
|------|------|
| **Rules** | 始终遵守的项目约束与协作规范 |
| **Skills** | 特定任务触发时读取的专项工作流 |

二者配合使用：Rules 定义「必须怎么做」，Skills 提供「具体怎么做」的详细流程与脚本。若冲突，以**更严格**的约定为准。
