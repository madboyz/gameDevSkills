# 配置表字段解析参考

## 表名与类型文件对应关系

| 来源 | 路径规则 | 用途 |
| :--- | :--- | :--- |
| 表名常量 | `tb.d.ts/AllFilenamePara.d.ts` → `tbp.fn.<表名>_` | 传给 `LD.getTB` / `LD.getLine` 的表名 |
| 字段常量 | `tb.d.ts/<表名>.d.ts` → `tbp.<表名>_.<字段>_` | `line.v_s(tbp.xxx_.field_)` 的字段名 |
| 字段语义 | `tb.d.tstype/tbp_<表名>.d.ts` | JSDoc 注释说明字段业务含义 |
| 字段类型 | `tb.d.ts/<表名>.d.ts` 注释括号 | 解析方式 |

## 读表 API（`@framework/core/LD`）

```typescript
// 整表
const tb = LD.getTB(tbp.fn.shijiexunshi_);
const allIds = tb.aIds;

// 单行
const line = LD.getLine(tbp.fn.shijiexunshi_, cityId);
const npcId = line.v_n(tbp.shijiexunshi_.npcId_);
const rewardStr = line.v_s(tbp.shijiexunshi_.jiangli_);

// 快捷读单元格
LD.v_n(tbp.fn.shijiexunshi_, cityId, tbp.shijiexunshi_.npcId_);
LD.v_s(tbp.fn.shijiexunshi_, cityId, tbp.shijiexunshi_.jiangli_);

// 整行灌入 type 结构
const row: tbp_shijiexunshi = {};
LD.gLineTypeD(tbp.fn.shijiexunshi_, cityId, row);
```

## 字段类型括号含义

| 括号标记 | 含义 | 推荐解析 |
| :--- | :--- | :--- |
| `(int)` | 整数 | `line.v_n(...)` 或 `Number(...)` |
| `(no)` | 数值编号（表 id / 枚举 id） | `line.v_n(...)`，再 `LD.getLine` 查关联表 |
| `(string)` | 原样字符串 | `line.v_s(...)` |
| `([_])` | 下划线区间，如 `1_10` | `str.split('_').map(Number)` |
| `([,_])` | 逗号+下划线复合，如 `1_2,3_4` | 先 `split(',')` 再按 `_` 拆 |
| `_NOT` 后缀（tbp 注释） | 策划标注「前端不读/不展示」 | 需求文档注明「仅后端或展示忽略」 |

## 常见复合字段

| 字段形态 | 解析入口 | 说明 |
| :--- | :--- | :--- |
| 奖励串 `jiangli_` | `GoodsUtil.getItemListByString(str)` | 默认 `类型_id_数量`，`|` 分隔多条 |
| 道具单价等 | `GoodsUtil.getItemByString(str, parseType)` | `parseType=0` 概率前缀；`1` 为倍数格式 |
| 赛季区间 `saiji_` | 自定义区间判断 | 与当前赛季比较是否在 `[min,max]` |

## 需求文档中的字段描述格式

每个字段写三行：

```markdown
#### `字段名_`（中文名）
- **类型**：`(int)` / ...
- **含义**：来自 tbp 注释 + 策划 docx 补充
- **解析**：`line.v_n(tbp.xxx_.field_)` 或 `GoodsUtil...`；注明关联表/模块
```
