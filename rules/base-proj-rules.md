---
trigger: always_on
---

# 项目结构与编码规范

本规则定义了项目的目录结构规范、代码组织方式以及命名约定。所有开发人员在编写代码时必须遵循这些规范。

---

## 一、目录结构概览

```
assets/scripts/
├── framework/          # 底层框架代码（引擎无关的通用功能）
│   ├── cache/          # 缓存管理
│   ├── core/           # 核心功能
│   ├── ecs/            # 实体组件系统
│   ├── enum/           # 通用枚举定义
│   ├── event/          # 事件系统
│   ├── net/            # 网络通信底层
│   ├── number/         # 数值处理
│   ├── render/         # 渲染相关
│   ├── resload/        # 资源加载
│   ├── scene/          # 场景管理
│   ├── timer/          # 定时器
│   └── utils/          # 工具类
├── logic/              # 业务逻辑代码
│   ├── enum/           # 业务枚举定义
│   ├── manager/        # 业务管理器
│   ├── net/            # 业务网络协议
│   ├── netdata/        # 网络数据模型
│   ├── opensys/        # 开放系统
│   ├── plugins/        # 插件
│   ├── scene/          # 业务场景
│   ├── uilayer/        # UI界面层
│   ├── uipara/         # UI参数配置
│   └── utils/          # 业务工具类
├── gamestart/          # 游戏启动相关
├── GDGlobal.ts         # 全局定义
└── GameDirect.ts       # 游戏主入口
```

---

## 二、代码分层规范

### 1. Framework 层（底层框架）

**位置**: `assets/scripts/framework/`

**职责**:
- 提供与具体业务无关的通用功能
- 封装引擎底层能力（基于 Cocos Creator 3.8.8）
- 提供可复用的基础组件和工具

**重要约束** ⚠️:
- **禁止在 framework 中 import 非 framework 文件夹的内容**
- framework 层必须保持独立性，不依赖业务逻辑
- 仅允许 import 引擎 API 和 framework 内部模块

**示例**:
```typescript
// ✅ 正确：仅引用 framework 内部
import { EventManager } from "@framework/event/EventManager";
import { TimerManager } from "@framework/timer/TimerManager";

// ❌ 错误：禁止引用 logic 层
import { SomeManager } from "@logic/manager/SomeManager"; // 禁止！
```

**子目录功能分类**:
| 目录 | 用途 |
|------|------|
| `cache/` | 缓存管理器、数据缓存策略 |
| `core/` | 核心基类、单例模式、基础数据结构 |
| `ecs/` | ECS 架构相关（Entity、Component、System） |
| `enum/` | 框架级通用枚举 |
| `event/` | 事件派发、监听机制 |
| `net/` | Socket 连接、协议解析底层 |
| `number/` | 数值计算、精度处理 |
| `render/` | 渲染优化、批处理 |
| `resload/` | 资源加载、Bundle 管理 |
| `scene/` | 场景生命周期管理 |
| `timer/` | 定时器、帧循环 |
| `utils/` | 通用工具函数 |

---

### 2. Logic 层（业务逻辑）

**位置**: `assets/scripts/logic/`

**职责**:
- 实现具体业务功能
- 处理游戏逻辑和 UI 交互
- 管理业务数据和状态

**子目录功能分类**:
| 目录 | 用途 |
|------|------|
| `enum/` | 业务相关枚举定义 |
| `manager/` | 业务管理器（如：玩家管理、战斗管理） |
| `net/` | 业务协议处理、网络消息Handler |
| `netdata/` | 网络数据模型、协议数据结构 |
| `opensys/` | 功能开放系统 |
| `plugins/` | 第三方插件集成 |
| `scene/` | 业务场景逻辑 |
| `uilayer/` | **UI界面实现**（所有 UI 相关代码在此） |
| `uipara/` | UI 参数配置、界面配置表 |
| `utils/` | 业务工具类 |

**UI 开发规范**:
- 所有 UI 界面类请在 `uilayer/` 目录下编写
- 按功能模块建立子目录组织 UI 代码
- UI 脚本应以功能名称命名，如 `Login.ts`、`Battle.ts`

---

### 3. GameStart 层（启动流程）

**位置**: `assets/scripts/gamestart/`

**职责**:
- 处理游戏初始化流程
- 资源预加载
- 启动阶段的状态管理

---

## 三、路径别名配置

当模块内容较多或需要频繁跨目录引用时，应在配置文件中添加路径别名。

### 1. tsconfig.json

```json
{
  "compilerOptions": {
    "paths": {
      "@framework/*": ["./assets/scripts/framework/*"],
      "@logic/*": ["./assets/scripts/logic/*"],
      "@gamestart/*": ["./assets/scripts/gamestart/*"]
      // 新增大型模块时在此添加
    }
  }
}
```

### 2. import-map.json

```json
{
  "imports": {
    "@framework/": "./assets/scripts/framework/",
    "@logic/": "./assets/scripts/logic/",
    "@gamestart/": "./assets/scripts/gamestart/"
    // 新增大型模块时同步添加
  }
}
```

**添加新别名的条件**:
- 模块内容较多（超过 10 个文件）
- 需要被多处频繁引用
- 跨越多层目录结构

---

## 四、命名规范

### 1. 文件夹命名

- **全部使用小写字母**
- 多个单词使用连接，不使用驼峰
- 语义清晰，见名知意

**示例**:
```
✅ 正确: uilayer, netdata, resload, gamestart
❌ 错误: UILayer, NetData, ResLoad, GameStart
```

### 2. TypeScript 文件命名

- **使用大驼峰命名（PascalCase）**
- 文件名应与主要导出类名一致
- 使用 `.ts` 后缀

**示例**:
```
✅ 正确: EventManager.ts, BundleResMng.ts, ViewLogin.ts
❌ 错误: eventManager.ts, bundle-res-mng.ts, view_login.ts
```

### 3. 命名对照表

| 类型 | 规范 | 示例 |
|------|------|------|
| 文件夹 | 全小写 | `framework`, `uilayer`, `netdata` |
| TS文件 | 大驼峰 | `GameDirect.ts`, `EventManager.ts` |
| 类名 | 大驼峰 | `class EventManager`, `class ViewLogin` |
| 接口 | I前缀+大驼峰 | `interface IEventHandler` |
| 常量 | 全大写+下划线 | `const MAX_COUNT = 100` |
| 变量/函数 | 小驼峰 | `let playerName`, `function getData()` |

### 4. 接口（interface）注释规范

**要求**：
- **`interface` 声明必须有注释**：紧挨在接口声明上方，不得省略。
- **内容两件事**：简明说明**接口职责/作用**，并给出**至少一条典型用法范例**（可写在 `@example` 中或短行内）。
- **风格**：用词精炼，不写冗长段落；范例需与真实字段/调用方式一致，避免无意义占位符堆砌。

**推荐写法（JSDoc）**：
```typescript
/**
 * 玩家背包中单个格子的可读视图，用于 UI 绑定与存档展示。
 * @example
 * const slot: IBagSlot = { goodsNo: 1001, count: 3 };
 */
export interface IBagSlot {
    goodsNo: number;
    count: number;
}
```

**反例**：
```typescript
// ❌ 无注释
export interface IEventHandler {
    onEvent(): void;
}

// ❌ 只有「接口定义」四字或复制类名，无作用说明、无范例
/** IEventHandler 接口 */
export interface IEventHandler { }
```

---

## 五、开发检查清单

在提交代码前，请确认以下检查项：

- [ ] 业务代码是否放在 `logic/` 目录下对应的子目录中
- [ ] UI 相关代码是否在 `logic/uilayer/` 中
- [ ] 底层框架代码是否在 `framework/` 中
- [ ] `framework/` 中是否有引用 `logic/` 或其他业务代码的 import（禁止）
- [ ] 新文件夹是否使用全小写命名
- [ ] 新 TS 文件是否使用大驼峰命名
- [ ] 大型模块是否已在 `tsconfig.json` 和 `import-map.json` 中配置别名
- [ ] **代码中使用 `new Node()` 创建节点时是否设置了 layer 层级**（参考 `framework/enum/EventBaseType.ts` 中的 `NodeLayer` 枚举）
- [ ] 使用 FairyGUI 时是否采用 `import * as fgui from 'fairygui-cc'`，并通过 `fgui.xxx` 访问类型（见「七、FGUI 导入规范」）
- [ ] 新增或修改的 **`interface` 是否已写注释**（含作用说明与范例，见「四、4. 接口（interface）注释规范」）

---

## 六、ECS 模块开发规范

ECS（Entity-Component-System）架构的代码需遵循以下规范：

### 1. 组件（Component）规范

**命名规则**:
- 类名/文件名必须以 `Comp` 开头
- 示例：`CompSprite.ts`、`CompTransform.ts`、`CompHealth.ts`

**类修饰符**:
- 必须在类定义的上一行添加 `@ecs.ECSClass("类名")` 修饰符
- 用于类注册，防止代码混淆后找不到类名

**示例**:
```typescript
// ✅ 正确写法
@ecs.ECSClass("CompSprite")
export class CompSprite extends Comp {
    // 组件实现
}

// ❌ 错误写法：缺少修饰符
export class CompSprite extends Comp {
    // ...
}

// ❌ 错误写法：命名不规范
@ecs.ECSClass("SpriteComp")
export class SpriteComp extends Comp {
    // ...
}
```

**文件存放位置**:

| 类型 | 存放路径 |
|------|----------|
| 底层框架组件（与业务无关） | `framework/ecs/comp/` |
| 业务逻辑组件 | `logic/ecs/comp/` |

---

### 2. 系统（System）规范

**命名规则**:
- 类名/文件名必须以 `Sys` 开头
- 示例：`SysRender.ts`、`SysMovement.ts`、`SysBattle.ts`

**类修饰符**:
- 必须在类定义的上一行添加 `@ecs.ECSClass("类名")` 修饰符
- 用于类注册，防止代码混淆后找不到类名

**示例**:
```typescript
// ✅ 正确写法
@ecs.ECSClass("SysRender")
export class SysRender extends System {
    // 系统实现
}

// ❌ 错误写法：缺少修饰符
export class SysRender extends System {
    // ...
}

// ❌ 错误写法：命名不规范
@ecs.ECSClass("RenderSystem")
export class RenderSystem extends System {
    // ...
}
```

**文件存放位置**:

| 类型 | 存放路径 |
|------|----------|
| 底层框架系统（与业务无关） | `framework/ecs/system/` |
| 业务逻辑系统 | `logic/ecs/system/` |

---

### 3. ECS 目录结构

```
assets/scripts/
├── framework/
│   └── ecs/
│       ├── comp/           # 底层框架组件
│       │   ├── CompSprite.ts
│       │   └── CompTransform.ts
│       ├── system/         # 底层框架系统
│       │   └── SysRender.ts
│       └── ECSCore.ts      # ECS 核心
└── logic/
    └── ecs/
        ├── comp/           # 业务逻辑组件
        │   └── CompPlayer.ts
        └── system/         # 业务逻辑系统
            └── SysBattle.ts
```

---

### 4. ECS 开发检查清单

- [ ] 组件类名/文件名是否以 `Comp` 开头
- [ ] 系统类名/文件名是否以 `Sys` 开头
- [ ] 是否添加了 `@ecs.ECSClass("类名")` 修饰符
- [ ] 修饰符中的字符串参数是否与类名一致
- [ ] 底层框架 ECS 代码是否在 `framework/ecs/` 目录下
- [ ] 业务逻辑 ECS 代码是否在 `logic/ecs/` 目录下

---

### 5. ECS System自动注册事件
使用 `@ecs.ECSEvent(事件常量)` 标注处理方法，`enable` 时自动注册，`disable` 时取消注册。

---

### 6. System 优先级排序

通过 `priority` 属性动态调整 System 执行顺序：

```typescript
const sysRender = world.getSys<SysRender>("SysRender");
sysRender.priority = 100;  // 数值越小越先执行

const sysPhysics = world.getSys<SysPhysics>("SysPhysics");
sysPhysics.priority = 50;  // 将在 sysRender 之前执行
```

| 规则 | 说明 |
|------|------|
| 数值越小 | 执行越靠前 |
| 默认值 | 0 |
| 生效时机 | 修改后下一帧生效（懒排序） |
| 相同优先级 | 保持原有添加顺序 |

---

## 七、FGUI（FairyGUI）导入规范

业务 UI 及需要引用 FairyGUI API 的代码，统一按下列方式导入与使用，避免零散具名导入、便于识别第三方 UI 类型来源。

### 导入方式

- **必须**使用命名空间导入：

```typescript
import * as fgui from 'fairygui-cc';
```

- **禁止**在同一规范下混用与上述不一致的导入风格（例如单独 `import { GComponent } from 'fairygui-cc'`），新代码一律走 `fgui` 命名空间。

### 使用方式

- FairyGUI 导出的类、枚举、工具等，一律通过 **`fgui.`** 前缀访问。
- 示例：`GComponent` → `fgui.GComponent`，`GObject` → `fgui.GObject`，`UIConfig` → `fgui.UIConfig`。

```typescript
import * as fgui from 'fairygui-cc';

// ✅ 正确
function bindRoot(root: fgui.GComponent): void {
    const child = root.getChild('btn') as fgui.GButton;
}

// ✅ 正确：继承 FairyGUI 组件
export class ViewExample extends fgui.GComponent {
    protected onConstruct(): void { }
}

// ❌ 错误：与项目统一的命名空间风格不一致
import { GComponent, GButton } from 'fairygui-cc';
```

### 适用范围

- 主要涉及 `logic/uilayer/`、`logic/utils/` 下与 FGUI 相关的脚本；其他目录若引用 `fairygui-cc`，同样遵循本节规则。

---

## 八、补充说明

### 引擎约束
- 项目基于 **Cocos Creator 3.8.8** 引擎
- 所有框架层代码需兼容 Cocos Creator 3.x API
- 禁止使用超出引擎能力范围的方案

### 官方文档
- **用户手册**: [https://docs.cocos.com/creator/3.8/manual/zh/](https://docs.cocos.com/creator/3.8/manual/zh/)
- **API 文档**: [https://docs.cocos.com/creator/3.8/api/zh/](https://docs.cocos.com/creator/3.8/api/zh/)

### 文档要求
- 重大变更需更新 README.md
- 实施前需规划确认