---
name: ecs-logic-development
description: 基于 ECS 框架编写游戏逻辑的规范和指南
---

# ECS 逻辑开发技能

本技能提供基于项目 ECS（Entity-Component-System）框架编写游戏逻辑的完整规范和最佳实践。

---

## 一、ECS 核心概念

### 1. 架构模式
本项目采用 **SOA（Structure of Arrays）** 存储模式的 ECS 架构：

```
World（世界）
  ├── System（系统）     → 处理逻辑
  ├── Entity（实体）     → 组件容器
  ├── Component（组件）  → 纯数据
  ├── DataCenter（数据中心） → 共享数据
  ├── Archetype（原型）  → 按组件组合分类实体
  └── ComponentStorage（组件存储器） → SOA 连续数组存储
```

### 2. 核心文件位置

| 模块 | 路径 |
|------|------|
| ECS 核心 | `@framework/ecs/ECSCore.ts` |
| 框架组件 | `@framework/ecs/comp/` |
| 框架系统 | `@framework/ecs/system/` |
| 业务组件 | `@logic/ecs/comp/` |
| 业务系统 | `@logic/ecs/system/` |
| 业务工厂 | `@logic/ecs/LogicECSFactory.ts` |
| 组件过滤器 | `@framework/ecs/BaseFilter.ts`、`@logic/ecs/LogicFilter.ts` |

### 3. 代码分层约束

> [!CAUTION]
> **Framework 层禁止引用 Logic 层代码**
> 
> `framework/ecs/` 目录下的所有代码（包括组件、系统、工具类）**严禁** import 任何 `logic/` 目录下的模块。
> 这是保证框架层独立性和可复用性的核心约束。

```typescript
// ✅ 正确：framework 中只引用 framework 和引擎模块
import { ecs } from "@framework/ecs/ECSCore";
import { CommonPool } from "@framework/cache/CommonPool";
import { Node } from "cc";

// ❌ 错误：framework 中禁止引用 logic
import { LogicFilter } from "@logic/ecs/LogicFilter";        // 禁止！
import { DataCenterGame } from "@logic/ecs/datacenter/...";  // 禁止！
```

**分层规则总结**：

| 层级 | 可引用 | 禁止引用 |
|------|--------|----------|
| `framework/ecs/` | `framework/*`、`cc`（引擎） | `logic/*`、`gamestart/*` |
| `logic/ecs/` | `framework/*`、`logic/*`、`cc` | - |

---

## 二、命名规范

### 1. 组件（Component）

- **类名/文件名必须以 `Comp` 开头**
- **必须添加 `@ecs.ECSClass("类名")` 修饰符**

```typescript
// ✅ 正确示例
import { ecs } from "@framework/ecs/ECSCore";

@ecs.ECSClass("CompHealth")
export class CompHealth extends ecs.Comp {
    public hp: number = 100;
    public maxHp: number = 100;
    
    reset(): void {
        this.hp = 100;
        this.maxHp = 100;
    }
}

// ❌ 错误示例
export class HealthComponent extends ecs.Comp { } // 命名不规范
export class CompHealth extends ecs.Comp { }      // 缺少装饰器
```

### 2. 系统（System）

- **类名/文件名必须以 `Sys` 开头**
- **必须添加 `@ecs.ECSClass("类名")` 修饰符**

```typescript
// ✅ 正确示例
import { ecs } from "@framework/ecs/ECSCore";

@ecs.ECSClass("SysBattle")
export class SysBattle extends ecs.System {
    onEntityAdd(entity: ecs.Entity): void { }
    onEntityRemove(entity: ecs.Entity): void { }
    onUpdate(dt: number): void { }
    reset(): void { }
}

// ❌ 错误示例
export class BattleSystem extends ecs.System { } // 命名不规范
```

### 3. 数据中心（DataCenter）

- **类名/文件名以 `DataCenter` 开头或包含 `DataCenter`**
- **必须添加 `@ecs.ECSClass("类名")` 修饰符**

```typescript
@ecs.ECSClass("DataCenterBattle")
export class DataCenterBattle extends ecs.DataCenter {
    public currentWave: number = 0;
    
    protected init(world: ecs.World, ...args: any[]): void {
        super.init(world, ...args);
    }
    
    reset(): void {
        this.currentWave = 0;
    }
}
```

---

## 三、创建流程

### 1. 创建组件

```typescript
// 文件路径：assets/scripts/logic/ecs/comp/CompPlayer.ts
import { ecs } from "@framework/ecs/ECSCore";
import { Vec3 } from "cc";

@ecs.ECSClass("CompPlayer")
export class CompPlayer extends ecs.Comp {
    // 属性定义
    public level: number = 1;
    public exp: number = 0;
    public position: Vec3 = new Vec3();
    
    // 必须实现 reset 方法，用于对象池复用时重置状态
    reset(): void {
        this.level = 1;
        this.exp = 0;
        this.position.set(0, 0, 0);
    }
}
```

### 2. 创建系统

```typescript
// 文件路径：assets/scripts/logic/ecs/system/SysPlayer.ts
import { ecs } from "@framework/ecs/ECSCore";
import { CompPlayer } from "../comp/CompPlayer";

@ecs.ECSClass("SysPlayer")
export class SysPlayer extends ecs.System {
    // 可选：设置更新间隔（帧数），默认为 1
    // 例如设置为 2 表示每隔 2 帧执行一次 onUpdate
    // protected _updateInterval: number = 1;
    
    /** 系统启用时调用 */
    enable(world: ecs.World): void {
        super.enable(world);
        // 初始化逻辑
    }
    
    /** 系统禁用时调用 */
    disable(): void {
        super.disable();
        // 清理逻辑
    }
    
    /** 实体添加到 World 时调用 */
    onEntityAdd(entity: ecs.Entity): void {
        const comp = entity.getComp<CompPlayer>("CompPlayer");
        if (comp) {
            // 处理玩家实体添加
        }
    }
    
    /** 实体从 World 移除时调用 */
    onEntityRemove(entity: ecs.Entity): void {
        // 清理逻辑
    }
    
    /** 每帧更新（受 _updateInterval 控制） */
    onUpdate(dt: number): void {
        // 使用 filter 查询关心的实体
        const entities = this.curWorld.filter(["CompPlayer"]);
        for (const entity of entities) {
            const comp = entity.getComp<CompPlayer>("CompPlayer");
            // 更新逻辑
        }
    }
    
    /** 回收时重置状态 */
    reset(): void {
        // 重置内部状态
    }
}
```

### 3. 定义组件筛选器（Filter）

在 `LogicFilter.ts` 中定义常用的组件组合：

```typescript
// 文件路径：assets/scripts/logic/ecs/LogicFilter.ts
export class LogicFilter {
    // 玩家相关组件
    public static PLAYER_COMPS: string[] = [
        "CompPlayer",
        "CompSceneObj",
        "CompSceneNode"
    ];
    
    // 敌人相关组件
    public static ENEMY_COMPS: string[] = [
        "CompEnemy",
        "CompHealth",
        "CompSceneObj"
    ];
}
```

---

## 四、API 使用指南

### 1. World（世界）操作

```typescript
// 创建世界
const world = ecs.createCommonWorld("GameWorld");
world.init(targetNode);

// 添加系统（按依赖顺序添加）
const sysPlayer = world.addSys<SysPlayer>("SysPlayer");
sysPlayer.enable(world);

// 添加数据中心
const dataCenter = world.addDataCenter<DataCenterGame>("DataCenterGame");

// 获取系统
const sys = world.getSys<SysPlayer>("SysPlayer");

// 获取数据中心
const data = world.getDataCenter<DataCenterGame>("DataCenterGame");

// 每帧更新（在场景 update 中调用）
world.update(dt, true); // dt 为帧间隔，isMs 表示是否转换为毫秒

// 暂停/恢复
world.pause = true;  // 暂停
world.pause = false; // 恢复

// 回收世界
world.recover();
```

### 2. Entity（实体）操作

```typescript
// 创建实体（推荐使用 Filter 预定义组件组合）
const entity = ecs.createCommonEntity(LogicFilter.PLAYER_COMPS);

// 或手动添加组件
const entity = ecs.createCommonEntity();
entity.addComp<CompPlayer>("CompPlayer");
entity.addComp<CompSceneObj>("CompSceneObj");

// 批量添加组件（性能优化：只触发一次 Archetype 更新）
entity.addComps(["CompA", "CompB", "CompC"]);

// 获取组件
const comp = entity.getComp<CompPlayer>("CompPlayer");

// 移除组件
entity.removeComp("CompPlayer");

// 批量移除组件
entity.removeComps(["CompA", "CompB"]);

// 添加到世界
world.addEntity(entity);

// 从世界移除
world.removeEntity(entity);
// 或通过 UUID
world.removeEntityByUUid(entity.uuid);
```

### 3. Filter（筛选）操作

```typescript
// 基础筛选（必须包含所有指定组件的实体）
const entities = world.filter(["CompPlayer", "CompHealth"]);

// 带排除条件的筛选
const entities = world.filter(
    ["CompSceneObj"],           // 必须包含
    ["CompPlayer", "CompNPC"]   // 排除
);
```

### 4. 事件系统

**自动事件注册**：System 中以 `EVENT_ECS` 开头的方法会在 `enable` 时自动注册，`disable` 时自动注销。

```typescript
@ecs.ECSClass("SysHUD")
export class SysHUD extends ecs.System {
    // 自动注册为 "EVENT_ECS_PLAYER_LEVEL_UP" 事件监听器
    EVENT_ECS_PLAYER_LEVEL_UP(newLevel: number): void {
        console.log(`玩家升级到 ${newLevel} 级`);
    }
    
    // 在其他系统中派发事件
    someMethod(): void {
        this.dispatchEvent("EVENT_ECS_PLAYER_LEVEL_UP", 10);
    }
}
```

---

## 五、工厂模式

推荐使用工厂类封装复杂实体的创建逻辑：

```typescript
// 文件路径：assets/scripts/logic/ecs/LogicECSFactory.ts
import { ecs } from "@framework/ecs/ECSCore";
import { LogicFilter } from "./LogicFilter";

export class LogicECSFactory {
    /**
     * 创建玩家实体
     */
    public static createPlayer(name: string): ecs.Entity {
        const entity = ecs.createCommonEntity(LogicFilter.PLAYER_COMPS);
        
        const compPlayer = entity.getComp<CompPlayer>("CompPlayer");
        compPlayer.name = name;
        
        const compSceneObj = entity.getComp<CompSceneObj>("CompSceneObj");
        compSceneObj.x = 0;
        compSceneObj.y = 0;
        
        return entity;
    }
    
    /**
     * 创建敌人实体
     */
    public static createEnemy(type: number, pos: Vec2): ecs.Entity {
        const entity = ecs.createCommonEntity(LogicFilter.ENEMY_COMPS);
        
        const compEnemy = entity.getComp<CompEnemy>("CompEnemy");
        compEnemy.type = type;
        
        const compSceneObj = entity.getComp<CompSceneObj>("CompSceneObj");
        compSceneObj.x = pos.x;
        compSceneObj.y = pos.y;
        
        return entity;
    }
}
```

---

## 六、性能优化建议

### 1. 更新间隔控制

对于不需要每帧更新的系统，设置 `_updateInterval`：

```typescript
@ecs.ECSClass("SysAI")
export class SysAI extends ecs.System {
    // 每 5 帧更新一次 AI
    protected _updateInterval: number = 5;
}
```

### 2. 优先级排序

动态调整 System 执行顺序，通过 `priority` 属性控制：

```typescript
// 获取 System 并设置优先级
const sysRender = world.getSys<SysRender>("SysRender");
sysRender.priority = 100;  // 数值越小越先执行

const sysPhysics = world.getSys<SysPhysics>("SysPhysics");
sysPhysics.priority = 50;  // 将在 sysRender 之前执行

// 执行顺序：sysPhysics(50) → sysRender(100)
```

**优先级规则**：
- 数值越小，执行越靠前
- 默认优先级为 0
- 相同优先级保持原有添加顺序（稳定排序）
- 修改后在下一帧生效（懒排序）

### 3. 批量操作

添加/移除多个组件时使用批量方法：

```typescript
// ✅ 推荐：只触发一次 Archetype 更新
entity.addComps(["CompA", "CompB", "CompC"]);

// ❌ 不推荐：触发三次 Archetype 更新
entity.addComp("CompA");
entity.addComp("CompB");
entity.addComp("CompC");
```

### 3. 缓存筛选结果

高频调用的筛选建议缓存：

```typescript
@ecs.ECSClass("SysRender")
export class SysRender extends ecs.System {
    private _renderEntities: ecs.Entity[] = [];
    
    onUpdate(dt: number): void {
        // 每帧重新获取（filter 有帧级缓存）
        this._renderEntities = this.curWorld.filter(["CompSprite"]);
        
        for (const entity of this._renderEntities) {
            // 渲染逻辑
        }
    }
}
```

### 4. SOA 批量遍历

利用 SOA 存储的连续内存访问优势：

```typescript
// 直接遍历某类型的所有组件（缓存友好）
world.forEachComponent<CompSprite>("CompSprite", (comp, entityUuid) => {
    if (comp.needLoad) {
        // 处理需要加载的精灵
    }
});
```

---

## 七、常见框架组件

| 组件 | 用途 |
|------|------|
| `CompSceneObj` | 场景对象基础属性（位置、透明度等） |
| `CompSceneNode` | Cocos Node 引用 |
| `CompSprite` | 精灵渲染配置 |
| `CompSceneCamera` | 相机控制 |
| `CompSceneCulling` | 场景裁剪 |
| `CompNeedSort` | 渲染排序 |

---

## 八、开发检查清单

在提交代码前确认：

- [ ] 组件类名/文件名以 `Comp` 开头
- [ ] 系统类名/文件名以 `Sys` 开头
- [ ] 已添加 `@ecs.ECSClass("类名")` 修饰符
- [ ] 修饰符中的字符串与类名一致
- [ ] 组件实现了 `reset()` 方法
- [ ] 系统实现了所有抽象方法
- [ ] 底层框架代码在 `framework/ecs/` 目录
- [ ] 业务逻辑代码在 `logic/ecs/` 目录
