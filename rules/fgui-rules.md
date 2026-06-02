---
description: FairyGUI（fgui）须以 fairygui.mjs 与项目内 Demo 为准，禁止臆测 API；Cocos 3.x 资源接口对齐。
globs:
  - assets/scripts/logic/uilayer/**/*.ts
  - assets/scripts/logic/uipara/**/*.ts
  - assets/scripts/fgui/**
---

# FairyGUI（fgui）开发规则

## 权威来源（必须对照）

1. **引擎实现**：回答或修改与 FairyGUI 行为、API、列表相关的逻辑时，必须先核对 `assets/scripts/fgui/fairygui.mjs`（本仓库实际运行的 fgui 实现），不得凭记忆或其他版本文档臆造签名或行为。
2. **用法示范**：本项目中 **虚拟列表** 的接入方式以业务代码里的用法为准（见下文「项目 Demo」），优于网络教程或旧版示例。

## 用户问「如何实现虚拟列表」时的标准答案来源

从 **项目 Demo** 中提取并复述下列顺序与模式（与 `fairygui.mjs` 中 `GList` 一致：`numItems` 赋值前若未设置 `itemRenderer` 会抛错，见源码 `set numItems`）。

### 项目 Demo（须优先引用）

- `assets/scripts/logic/uilayer/mail/Mail.ts`：`setExtension` → `setVirtual()` → `itemRenderer` → `on(CLICK_ITEM)` → `numItems`；选中项变更后使用 `refreshVirtualList()`。
- `assets/scripts/logic/uilayer/gm/GmTemp.ts`：同上核心四步（`setVirtual`、`itemRenderer`、`CLICK_ITEM`、`numItems`），列表数据为 `this.list.length`。

### 与 Demo 对齐的要点（从 Demo 归纳）

1. 自定义列表项类通过 `fgui.UIObjectFactory.setExtension('ui://包名/资源名', ItemClass)` 注册（Demo 中包路径与类名以实际界面为准）。
2. 取得 `fgui.GList` 后调用 `list.setVirtual()` 开启虚拟列表。
3. 赋值 `list.itemRenderer = this.renderListItem.bind(this)`（或等价绑定），回调签名为 `(index, item) => void`，在回调内用 `index` 从业务数据取数并刷新 `item`。
4. 再设置 `list.numItems = 数据源.length`（或当前数据条数）。**顺序**：先 `itemRenderer`，后 `numItems`（与源码约束一致）。
5. 列表项点击使用 `list.on(fgui.Event.CLICK_ITEM, ...)`（Demo 用法）；数据或选中态变化后若需重刷可见项，参考 `Mail.ts` 中的 `refreshVirtualList()` 用法。

未在 **本仓库 Demo** 中出现过的 `GList` / `fgui` API，不要随意推荐给业务代码；若确有需要，应在 `fairygui.mjs` 中确认存在且语义一致后再用。

## Cocos Creator 版本对齐

- 本客户端为 **Cocos Creator 3.x**；资源加载等引擎 API 以项目现有代码及 Demo 为准（例如 `assetManager`、`resources` 等 3.x 用法）。
- **禁止**在解答或示例中使用 Cocos 2.x 典型写法（如 `cc.loader`）作为本项目推荐方案，除非 `fairygui.mjs` 或业务层明确仍封装了等价旧接口（以仓库内实际代码为准）。

## 避坑指南（Constraints）

- **禁止幻觉**：Demo 未使用、且未在 `fairygui.mjs` 中核对的 API，尽量不要使用或编造参数。
- **版本对齐**：引擎侧以 Cocos 3.x 为准；**Demo 是业务层用法的最高优先级验证标准**。
