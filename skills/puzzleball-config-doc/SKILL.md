---
name: puzzleball-config-doc
description: 根据 game.js 源码分析 bin/res/puzzleball/config 中指定 JSON 配置的用途与使用逻辑，并生成说明文档。必须由用户指定要分析的 JSON 配置文件名。
---

# PuzzleBall 配置说明文档生成 Skill

## 前置条件（必须满足）

**用户必须明确指定要分析的 JSON 配置文件名**，例如：`boxShop.json`、`stageA.json`、`roleRefresh.json`。

若用户未指定配置名，应提示：

> 请指定要分析的 JSON 配置文件名，例如：boxShop.json、stageA.json、roleRefresh.json。  
> 可用的配置文件位于 `bin/res/puzzleball/config/` 目录下。

## 路径与映射

| 类型 | 路径 |
|------|------|
| 源码 | `origProj/__WITHOUT_MULTI_PLUGINCODE__.wxapkg_decrypt_unpack/game.js` |
| 配置目录 | `bin/res/puzzleball/config/` |
| 文档输出 | `docs/puzzleball-{配置名}-config.md`（如 `docs/puzzleball-boxShop-config.md`） |

## 配置名 → ConfigRoot 映射表

| JSON 配置 | ConfigUrl 属性 | ConfigRoot 属性 | 数据结构 |
|-----------|----------------|-----------------|----------|
| item.json | goods | goods | GoodsConfig |
| role.json | roleUrl | role | RoleConfig |
| roleSkill.json | skillUrl | skills | SkillConfig |
| stageReward.json | stageRewardUrl | stageReward | StageRewardConfig |
| dailyShopReward.json | storeBoxUrl | storeBoxMap | StoreBoxConfig |
| dailyShop.json | storeDailyshopUrl | storeDaily | StoreDailyshop |
| boxShop.json | storeBoxShopUrl | storeBoxShop | StoreBoxShop |
| buyGold.json | storeBuyGoldUrl | storeBuyGold | StoreBuyGold |
| dayTask.json | dayTaskUrl | dayTasks | DayTaskConfig |
| onlineReward.json | onlineRewardUrl | onlineReward | OnlineRewardConfig |
| signIn.json | signInUrl | signIn | SignInConfig |
| signInNew.json | signInNewUrl | signInNew | SignInNewConfig |
| plotOverview.json | plotUrl | plotConfigs | PlotConfig |
| global.json | paraUrl | paras | ParaConfig |
| monster.json | monsterUrl | monsters | MonsterConfig |
| artifact.json | atifactUrl | artifacts | ArtifactConfig |
| stage.json | chapterStageUrl | chapterStages | ChapterStageConfig |
| stageA.json | chapterStageUrl2 | chapterStages2 | ChapterStageConfig |
| stage1~7.json | stage1~7Url | stages[0~6] | StageConfig |
| stagEendless1~3.json | stageEendless1~3Url | stageEendlesss[0~2] | StageConfig |
| grade.json | battleLvUrl | battleLvs | BattleLvConfig |
| superRole.json | superRoleUrl | superRoles | SuperRoleConfig |
| bossSkill.json | bossSkillUrl | bossSkills | BossSkillConfig |
| roleRefresh.json | roleRefreshUrl | roleRefreshs | RoleRefreshConfig |
| buff.json | buffUrl | buffs | BuffConfig |
| stageEndlessReward.json | stageEndlessRewardUrl | stageEndlesssReward | StageRewardConfig |
| stageEndlessReward2.json | stageEndlessReward2Url | challengeMap | StageEndlessReward2Config |
| chat.json | portraitUrl | portraits | PortraitConfig |
| plotRole.json | plotRoleUrl | plotRoles | PlotRoleConfig |
| TalentData.json | talentUrl | talents | TalentConfig |
| dayGift.json | dayGiftUrl | dayGifts | DayGiftConfig |
| gameLevel.json | gameLevelUrl | gameLevels | GameLevelConfig |
| BatteryEliminationStage.json | bEStageConfigUrl | bEStageConfigs | BEStageConfig |
| BatteryEliminationMonster.json | bEMonsterConfigUrl | bEMonsterConfigs | BEMonsterConfig |
| BatteryEliminationLevel.json | bELevelConfigUrl | bELevelConfigs | BELevelConfig |
| shareReward.json | shareRewardUrl | shareRewards | ShareRewardConfig |

## 执行流程

### 1. 确认配置名

- 校验用户指定的配置名是否存在于 `bin/res/puzzleball/config/` 中
- 若不存在，提示可用配置列表

### 2. 定位 ConfigRoot 属性

- 根据映射表找到对应的 `ConfigRoot.xxx` 属性
- 在 game.js 中搜索该属性名（如 `storeBoxShop`、`chapterStages2`）

### 3. 分析源码使用逻辑

使用 Grep 在 game.js 中搜索：

```
ConfigRoot.{属性名}
```

对每个引用点：

- 读取上下文（前后若干行）
- 归纳：在什么场景下使用、读取了哪些字段、参与什么逻辑

### 4. 分析 JSON 结构

- 读取 `bin/res/puzzleball/config/{配置名}` 的 JSON 内容
- 提取字段名、类型、示例值
- 结合源码推断各字段含义

### 5. 生成文档

按以下结构输出到 `docs/puzzleball-{配置名}-config.md`：

```markdown
# PuzzleBall {配置用途}配置说明

本文档说明 puzzleball 玩法中 `{配置名}` 配置的用途、字段含义及源码中的使用方式。

## 一、配置文件

| 配置文件 | 用途 | 数据结构 |
|---------|------|----------|
| {配置名} | {简要用途描述} | {数据结构名} |

## 二、配置读取流程

### 2.1 加载入口

在 `ConfigRoot.init()` 中加载（game.js 约 31554-31590 行）：

[引用加载代码]

### 2.2 解析与存储

[说明 createMap/createList 及 key 字段]

## 三、数据结构

### 3.1 顶层字段

| 字段 | 类型 | 说明 |
|------|------|------|
| ... | ... | ... |

### 3.2 嵌套对象（如有）

[子对象字段表]

## 四、源码使用逻辑

### 4.1 使用场景 1

[描述 + 关键代码片段 + 行号]

### 4.2 使用场景 2

...

## 五、配置示例

[典型 JSON 示例 + 含义说明]

## 六、相关源码位置

| 功能 | 位置（game.js 行号） |
|------|---------------------|
| ... | ... |
```

## 搜索技巧

1. **ConfigRoot 属性**：`ConfigRoot.{属性名}` 或 `ConfigRoot.{属性名}.`
2. **ConfigUrl**：`ConfigUrl.{对应Url属性}` 定位加载路径
3. **配置类**：搜索 `createMap(ConfigUrl.xxx` 或 `createList(ConfigUrl.xxx` 确认解析方式
4. **key 字段**：createMap 默认用 `id` 作 key，部分用 `chatId` 等，需从 createMap 调用确认

## 参考示例

- `docs/puzzleball-boxShop-config.md`：商店宝箱配置
- `docs/puzzleball-roleRefresh-config.md`：角色抽卡权重配置

## 注意事项

- 源码为压缩混淆的 JS，变量名可能不直观，需结合上下文理解
- 同一配置可能被多处引用，需尽量覆盖所有使用点
- 字段说明需基于源码实际使用推断，避免臆测
