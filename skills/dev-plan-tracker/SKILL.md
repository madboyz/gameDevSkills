---
name: dev-plan-tracker
description: 维护本项目开发计划与交接记录。修改代码、实现计划、修复 bug、补齐功能、重构模块、调整接口或同步文档时使用；在任务结束前按主修改模块更新 doc/plan 下对应模块计划文件，记录目标、已完成内容、缺失内容、验证结果和后续入口。
---

# 开发计划维护技能

## 核心目标

在每次开发任务中，为当前变更留下可交接的计划记录。计划只记录本次任务的开发进度、已完成内容、缺失内容、验证结果和下次入口，不替代 `doc/` 下的专题设计文档。

## 使用流程

1. 在开始修改前识别本次任务的主模块。
2. 根据主模块确定 `doc/plan/<模块分类>/` 目录及目标计划文件（见下方「目标文件映射」）。
3. 在目标文件的「任务记录」下追加 `### 任务：<标题>` 节，并同步更新「待办总览」。
4. 开发过程中持续更新：完成一项记录到任务节「已完成」，发现未处理事项记录到「未完成 / 缺失内容」及「待办总览」。
5. 任务结束前补齐「已验证」和「下次接手建议」。
6. 如果本次变更触发项目文档维护规则，仍需同步对应专题文档；`doc/plan` 只作为进度与交接记录。

## 路径分类规则

优先按主要修改文件所属业务路径映射：

- `assets/scripts/logic/scene/map/*` -> `doc/plan/scene/map/`（按子模块选文件，见下）
- `assets/scripts/logic/scene/team/*` -> `doc/plan/scene/team/模块计划.md`
- `assets/scripts/logic/scene/hub/*` -> `doc/plan/scene/hub/模块计划.md`
- `assets/scripts/logic/scene/city/*` -> `doc/plan/scene/city/模块计划.md`
- `assets/scripts/logic/scene/chanye/*` -> `doc/plan/scene/chanye/模块计划.md`
- `assets/scripts/logic/uilayer/<module>/*` -> `doc/plan/uilayer/<module>/模块计划.md`
- `assets/scripts/framework/<module>/*` -> `doc/plan/framework/<module>/模块计划.md`
- `assets/scripts/gamestart/*` -> `doc/plan/gamestart/模块计划.md`
- `tools/excel_tips/*`、配置表规则 -> `doc/plan/tools/配置表工具计划.md`
- 跨多个模块时，选择本次任务的主行为模块；其余模块写入任务节「当前涉及文件」。

若没有明确匹配项，使用最接近的业务目录名生成分类，例如 `assets/scripts/logic/foo/bar/*` 对应 `doc/plan/foo/bar/模块计划.md`。目录名保持小写。

## 目标文件映射（scene/map 特殊）

`scene/map/` 目录按子模块选择目标文件，不共用单一 `模块计划.md`：

| 任务类型 | 目标文件 |
|---|---|
| 协议 Listener、Binder、GC_1350 等基础设施 | `doc/plan/scene/map/基础设施模块计划.md` |
| 寻路、路径、边权 | `doc/plan/scene/map/寻路模块计划.md` |
| 巡视进度、Hub 点击、1350/1353 联调 | `doc/plan/scene/map/巡视模块计划.md` |
| 巡视逻辑需求（logic-req-doc 产出） | `doc/plan/scene/map/巡视逻辑需求.md` |

## 文件命名

- 每个代码路径目录维护**一份**模块级主计划，默认文件名：`模块计划.md`。
- `scene/map/` 按上表使用 `基础设施模块计划.md`、`寻路模块计划.md`、`巡视模块计划.md`。
- `tools/` 使用 `配置表工具计划.md`。
- 逻辑需求文档（logic-req-doc 产出）使用 `<功能短名>逻辑需求.md`，与模块计划分开存放。
- **不再**每次任务新建独立 `<任务标题>计划.md` 文件；在模块计划内追加任务节。

## 模块计划模板

```markdown
# <模块名>开发计划

## 模块概览
- 职责边界、关键入口文件

## 待办总览
- [ ] 跨任务去重后的 open items

## 任务记录

### 任务：<短标题>（YYYY-MM-DD 可选）

#### 背景与目标
#### 当前涉及文件（可选）
#### 已完成
#### 未完成 / 缺失内容
#### 已验证
#### 下次接手建议

## 模块级接手建议
```

## 写作要求

- 使用简体中文。
- 内容以事实和下一步动作为主，不写泛泛总结。
- 追加任务时同步更新「待办总览」；矛盾项以最新任务/代码为准。
- 路径使用仓库相对路径。
- 对齐旧工程时写明具体参考文件，不把相近但不同的旧实现混为一套规则。
- 历史任务已合并进模块计划；维护时在对应模块文件内追加任务节，勿再创建独立任务文件。

## 索引

完整目录对照见 `doc/plan/README.md`。
