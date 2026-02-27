---
name: 配置数据结构定义
description: 根据源码和配置 JSON 文件定义 TypeScript 配置数据类型
---

# 配置数据结构定义 Skill

## 能力说明

此 Skill 用于根据源码 `origProj\__WITHOUT_MULTI_PLUGINCODE__.wxapkg_decrypt_unpack\game.js` 和配置 JSON 文件 `bin/res/puzzleball/config/` 定义 TypeScript 配置数据类型结构。

### 配置文件路径
- 已生成完整的配置 JSON 路径：`bin/res/puzzleball/config/`
- 所有配置文件都是 JSON 数组格式，包含多个配置对象

## 数据结构定义规范

### 类型定义格式
- **必须使用 `export type`**：数据结构不要用 `class xxx`，改为用 `export type xxx = {}`
- **参考案例**：数据结构定义参考 `src/script/puzzleball/config/ConfigRoot.ts` 已有案例定义

### 类型定义示例

```typescript
// ✅ 正确的定义方式
export type GoodsConfig = {
    id: number;
    name: string;
    type: number;
    des: string;
    qulity: number;
    stage: number;
}

// ❌ 错误的定义方式
class GoodsConfig {
    id: number;
    name: string;
    type: number;
    des: string;
    qulity: number;
    stage: number;
}
```

## 字段类型推断规则

### 基础类型推断

1. **数字类型 (number)**
   - 纯数字值：`"id": 1` → `id: number`
   - 负数：`"cost": -1` → `cost: number`

2. **字符串类型 (string)**
   - 文本值：`"name": "铜钱"` → `name: string`
   - 描述：`"des": "挂机收益道具"` → `des: string`

3. **布尔类型 (boolean)**
   - true/false 值：`"showHp": true` → `showHp: boolean`

4. **数组类型**
   - 数字数组：`"atack": [10, 13, 17]` → `atack: number[]`
   - 字符串数组：`"refreshLevel1": ["1", "2"]` → `refreshLevel1: string[]`
   - 混合数组：`"frame": [1, 2, 3]` → `frame: number[]`

5. **联合类型 (string | number)**
   - 在不同配置对象中，同一字段可能是字符串或数字
   - 示例：`"attribute": "10"` 或 `"attribute": 10` → `attribute: string | number`
   - 常见字段：`atkFrame`、`attribute` 等

### 可选字段规则

字段后添加 `?` 表示可选，当满足以下条件时：

1. **部分对象缺失该字段**
   ```typescript
   // 某些配置对象有 frame 字段，某些没有
   frame?: number[];
   ```

2. **字段值可能为 undefined**
   ```typescript
   // 某些配置对象该字段可能不存在
   artifact?: number;
   attribute?: number[];
   ```

### 特殊字段处理

1. **可选的声音字段**
   ```typescript
   atkSound: string;      // 必需
   atkSound2?: string;    // 可选
   skillSound?: string;   // 可选
   bigSkillSound?: string; // 可选
   ```

2. **可选的数组字段**
   ```typescript
   tailLength?: number[];
   bulletSize?: number[];
   ```

## 配置类型定义流程

### 步骤 1: 查看 JSON 配置文件
1. 定位到 `bin/res/puzzleball/config/` 目录
2. 找到对应的配置文件（如 `item.json`、`role.json` 等）
3. 分析 JSON 结构，查看所有字段

### 步骤 2: 参考源码实现
1. 打开源码 `origProj\__WITHOUT_MULTI_PLUGINCODE__.wxapkg_decrypt_unpack\game.js`
2. 搜索配置相关的加载和使用代码
3. 确认字段的实际用途和类型

### 步骤 3: 定义 TypeScript 类型
1. 在 `ConfigRoot.ts` 文件顶部添加类型定义
2. 使用 `export type` 格式
3. 根据 JSON 数据推断字段类型
4. 标记可选字段（使用 `?`）

### 步骤 4: 在 ConfigRoot 类中声明
1. 在 `ConfigRoot` 类中添加静态属性
2. 使用 `Map<number, XxxConfig>` 格式存储配置
3. 在 `loadConfig` 方法中加载配置

## 完整示例

### JSON 配置文件示例 (item.json)
```json
[
    {
        "id": 1,
        "name": "铜钱",
        "type": 1,
        "des": "挂机收益道具",
        "qulity": 2,
        "stage": 0
    },
    {
        "id": 2,
        "name": "元宝",
        "type": 1,
        "des": "通用高级货币",
        "qulity": 4,
        "stage": 0
    }
]
```

### TypeScript 类型定义
```typescript
export type GoodsConfig = {
    id: number;
    name: string;
    type: number;
    des: string;
    qulity: number;
    stage: number;
}
```

### ConfigRoot 类中使用
```typescript
export default class ConfigRoot {
    public static goods: Map<number, GoodsConfig> = new Map();

    public static async loadConfig(): Promise<void> {
        const configs = [
            { url: "res/puzzleball/config/item.json", type: Laya.Loader.JSON },
            // ... 其他配置
        ];

        return new Promise((resolve) => {
            Laya.loader.load(configs, Laya.Handler.create(null, () => {
                this.goods = this.createMap("res/puzzleball/config/item.json");
                // ... 其他配置加载
                resolve();
            }));
        });
    }

    private static createMap<T>(jsonUrl: string, keyName: string = "id"): Map<number, T> {
        const map = new Map<number, T>();
        const list = Laya.loader.getRes(jsonUrl) as T[];

        if (list) {
            list.forEach(item => {
                // @ts-ignore
                const key = item[keyName];
                map.set(key, item);
            });
        }
        return map;
    }
}
```

## 复杂配置示例

### 包含可选字段和数组的配置

**JSON 配置 (role.json)**
```json
{
    "key": 1,
    "id": 1001,
    "name": "石佛",
    "des": "石塑之佛，静镇一方",
    "qulity": 2,
    "type1": 2,
    "triggerNum": 1,
    "maxLevel": 15,
    "atack": [10, 13, 17, 23],
    "growup": [1, 2, 4, 8, 16],
    "shape": [1],
    "needItem": 1001,
    "needNum": [5, 10, 25, 50],
    "needGold": [100, 200, 500],
    "skillId": [10011, 10012],
    "unlockLv": [1, 3, 5, 7, 9],
    "stageID": 1,
    "cost": 10,
    "use": 1,
    "gridNum": 1,
    "atkSound": "role_1001_1",
    "atkSound2": "role_1001_1",
    "tailLength": [12, 12]
}
```

**TypeScript 类型定义**
```typescript
export type RoleConfig = {
    key: number;
    id: number;
    name: string;
    des: string;
    qulity: number;
    type1: number;
    triggerNum: number;
    maxLevel: number;
    atack: number[];
    growup: number[];
    shape: number[];
    needItem: number;
    needNum: number[];
    needGold: number[];
    skillId: number[];
    unlockLv: number[];
    stageID: number;
    cost: number;
    use: number;
    gridNum: number;
    atkSound: string;
    atkSound2?: string;          // 可选字段
    skillSound?: string;         // 可选字段
    bigSkillSound?: string;      // 可选字段
    tailLength?: number[];       // 可选字段
    bulletSize?: number[];       // 可选字段
}
```

## 常见配置类型

### 已定义的配置类型（参考 ConfigRoot.ts）

1. **GoodsConfig** - 物品配置
2. **MonsterConfig** - 怪物配置
3. **ChapterStageConfig** - 章节关卡配置
4. **StageConfig** - 关卡配置
5. **RoleConfig** - 角色配置
6. **SkillConfig** - 技能配置
7. **ParaConfig** - 参数配置
8. **SuperRoleConfig** - 超级角色配置
9. **ArtifactConfig** - 神器配置
10. **RoleRefreshConfig** - 角色刷新配置

### 待定义的配置类型（bin/res/puzzleball/config/ 中的其他文件）

- BatteryEliminationLevel
- BatteryEliminationMonster
- BatteryEliminationStage
- TalentData
- BossSkill
- BoxShop
- Buff
- BuyGold
- Chat
- DailyShop
- DailyShopReward
- DayGift
- DayTask
- GameLevel
- Grade
- OnlineReward
- PlotOverview
- PlotRole
- ShareReward
- SignIn
- SignInNew
- StageEndless
- StageReward

## 注意事项

### 命名规范
- 类型名使用 PascalCase：`GoodsConfig`、`RoleConfig`
- 字段名保持与 JSON 一致（可能是 camelCase 或 snake_case）
- 配置 Map 使用复数形式：`goods`、`monsters`、`roles`

### 类型安全
- 尽量精确定义类型，避免使用 `any`
- 可选字段必须标记 `?`
- 数组类型明确元素类型：`number[]` 而非 `any[]`

### 源码一致性
- 定义类型前必须查看源码中的实际使用方式
- 字段名必须与源码中使用的字段名完全一致
- 如果源码中有特殊处理逻辑，需要在注释中说明

### 配置加载
- 所有配置必须在 `loadConfig` 方法中加载
- 使用 `createMap` 方法创建配置 Map
- 默认使用 `id` 字段作为 key，特殊情况可指定其他字段

## 使用流程总结

1. **确认配置文件**：查看 `bin/res/puzzleball/config/` 中的 JSON 文件
2. **参考源码**：在 `game.js` 中搜索该配置的使用方式
3. **定义类型**：在 `ConfigRoot.ts` 顶部使用 `export type` 定义
4. **声明属性**：在 `ConfigRoot` 类中添加静态 Map 属性
5. **加载配置**：在 `loadConfig` 方法中添加加载逻辑
6. **验证正确性**：确保类型定义与 JSON 结构和源码使用一致
