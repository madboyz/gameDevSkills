---
name: logic-req-doc
description: 根据策划 .docx 文档、配置表（AllFilenamePara.d.ts / tb.d.tstype）、可选参考代码与 netdata 协议（PB*.ts / *.proto），生成前后端职责清晰、含读表伪逻辑与协议时序的详细逻辑需求文档。当用户要求「生成逻辑需求文档」「策划文档转开发需求」「根据 docx 写前端逻辑说明」或提供 docx + 表名 + 协议路径时使用。
---

# 逻辑需求文档生成 (logic-req-doc)

将策划 docx、配置表定义、参考代码与 protobuf 协议整合为**可交付开发**的逻辑需求文档（Markdown）。

## 用户输入清单

执行前确认输入；缺失**必须项**时先向用户索取，勿臆造表名或协议。

| 优先级 | 输入 | 示例 |
| :--- | :--- | :--- |
| **必须** | 策划 docx 路径 | `doc/策划文档/S世界地图相关/D地图巡视系统-覃茂政.docx` |
| **必须** | 数据表名（从 AllFilenamePara 查） | `shijiexunshi_` |
| **必须** | 各表字段含义与解析说明 | 用户 @ `tb.d.tstype/tbp_shijiexunshi.d.ts` 等；Agent 需再读 `tb.d.ts/<表名>.d.ts` 取类型括号 |
| 可选 | 参考代码片段或脚本 | 已有 Utils / Listener / UI 实现 |
| 可选 | 协议脚本 + 原始 proto | `assets/scripts/logic/netdata/PBworld.ts`、`protobuf/protofile/world.proto` |

## 执行流程

### 1. 提取策划文档

```bash
python .codex/skills/logic-req-doc/scripts/extract_docx.py "<docx绝对或相对路径>"
```

- 输出写入分析上下文；保留 `[表格]` 块结构。
- docx 不可读时告知用户路径或格式问题，停止编造需求。

### 2. 解析配置表

1. 在 `tb.d.ts/AllFilenamePara.d.ts` 的 `tbp.fn` 中核对表名常量（如 `shijiexunshi_`）。
2. 对每个表读取：
   - `tb.d.tstype/tbp_<表名去掉末尾_>.d.ts` — 字段中文含义
   - `tb.d.ts/<表名去掉末尾_>.d.ts` — 字段类型括号 `(int)` `(no)` `([_])` 等
3. 字段解析规则见 [tb-field-parsing.md](references/tb-field-parsing.md)。
4. 用 `codegraph_search` / `codegraph_context` 查找表中 id 引用的关联表、已有 `LD.getLine` 用法，写入「模块依赖」。

### 3. 解析协议（用户指定时）

1. 读 `protobuf/protofile/*.proto`：message 名、字段、注释中的状态枚举。
2. 读 `assets/scripts/logic/netdata/PB*.ts`：
   - `req*` / `sendMsg(协议号)` → CG
   - `NDGC_*` → GC 分发
3. 追踪 Listener：如 `PBworld.onListener` → `WorldMapProtocolListener.onGCxxxx`。
4. 在需求文档中写清：协议号、Message、触发时机、字段含义、前后端谁产生/消费该状态。

用户未指定但 docx 描述联网行为时，在「待确认项」列出推断的交互，**不伪造协议号**。

### 4. 吸收参考代码（可选）

- 对齐已有函数名、数据结构、事件名；在伪逻辑中直接引用（如 `getXunShiList()`）。
- 参考代码与 docx 冲突时，以 docx 为准并在「待确认项」标注差异。

### 5. 划分前后端职责

对每个功能点标注 **后端** / **前端** / **前后端**：

| 倾向后端 | 倾向前端 |
| :--- | :--- |
| 资格校验、发奖、战斗结算、持久化状态 | 读表展示、UI 状态、动画、本地预筛选、红点 |
| 协议中 GC 下发的 map/state | 纯客户端缓存、FGUI 布局、本地排序 |

### 6. 编写伪逻辑

每条核心流程必须包含：

- **输入/输出**
- **读表**：`LD.getTB` / `getLine` / `v_n` / `v_s` 及字段常量
- **玩家态**：如 `PBComData`、`MapData`、Listener 缓存
- **封装接口**：如 `GoodsUtil.getItemListByString`、`NetMng.i.sendMsg`
- **UI/模块落点**（若可推断）

命名用 camelCase 函数式描述；与参考代码一致时沿用原名。

### 7. 输出文档

1. 按 [output-template.md](references/output-template.md) 结构生成完整 Markdown。
2. 默认保存路径：`doc/plan/<模块>/` 或用户指定目录；文件名：`<功能短名>逻辑需求.md`。
3. 使用简体中文；协议号、表名、类型名保持代码原文。

## 质量检查（输出前自检）

- [ ] 必须输入均已使用，来源路径已写入文档头
- [ ] 每个涉及表均有字段说明（含义 + 类型 + 解析方式）
- [ ] 前后端职责表覆盖 docx 全部功能点
- [ ] 每条伪逻辑可追溯到表字段或协议字段
- [ ] 未指定协议处已标「待确认」，无虚构协议号
- [ ] 参考代码已对齐或标注冲突

## 示例触发语句

```
根据 @doc/策划文档/.../D地图巡视系统.docx，
表名 shijiexunshi_，字段见 @tb.d.tstype/tbp_shijiexunshi.d.ts，
协议 @PBworld.ts @world.proto，
参考 getXunShiList 的实现，生成逻辑需求文档。
```

## 参考资源

- [输出模板](references/output-template.md)
- [配置表字段解析](references/tb-field-parsing.md)
- 读表实现：`assets/scripts/framework/core/LD.ts`
- 奖励解析：`assets/scripts/logic/utils/goods/GoodsUtil.ts`
