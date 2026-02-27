---
name: 源码参考优先
description: 在功能移植、逻辑实现或问题排查时，优先参考源码确保实现的准确性和一致性
---

# 源码参考优先 Skill

## 核心原则

在 PuzzleBall 项目开发过程中，**源码是最权威的参考依据**。凡是不太确定的实现逻辑，必须参考源码 `origProj\__WITHOUT_MULTI_PLUGINCODE__.wxapkg_decrypt_unpack\game.js`，确保移植的准确性和一致性。

## 适用场景

以下情况必须优先查阅源码：

1. **功能移植**：从噩梦守护战移植功能到 PuzzleBall 项目
2. **逻辑实现**：实现某个模块或功能时对细节不确定
3. **问题排查**：遇到 bug 或异常行为需要定位原因
4. **接口定义**：不确定某个类、方法或数据结构的定义
5. **配置适配**：需要了解配置数据的使用方式
6. **行为验证**：需要确认某个功能的预期行为

## 工作流程

### 1. 明确查找目标

在查阅源码前，先明确你要查找的内容：

- **类名/方法名**：例如 `BrickEquip`、`initData`
- **功能模块**：例如装备系统、战斗管理器
- **数据结构**：例如装备配置、关卡数据
- **业务逻辑**：例如拖拽流程、碰撞检测

### 2. 在源码中定位

使用 `grep_search` 工具在源码中搜索目标：

```typescript
// 搜索类定义
grep_search({
  SearchPath: "e:/Project/baizhan_slg/baizhan_pro/tech_share/PuzzleBall/origProj/__WITHOUT_MULTI_PLUGINCODE__.wxapkg_decrypt_unpack/game.js",
  Query: "class BrickEquip",
  IsRegex: false,
  MatchPerLine: true
})

// 搜索方法定义
grep_search({
  SearchPath: "e:/Project/baizhan_slg/baizhan_pro/tech_share/PuzzleBall/origProj/__WITHOUT_MULTI_PLUGINCODE__.wxapkg_decrypt_unpack/game.js",
  Query: "initData\\s*\\(",
  IsRegex: true,
  MatchPerLine: true
})
```

### 3. 查看源码实现

使用 `view_file` 查看具体实现：

```typescript
// 查看特定行范围
view_file({
  AbsolutePath: "e:/Project/baizhan_slg/baizhan_pro/tech_share/PuzzleBall/origProj/__WITHOUT_MULTI_PLUGINCODE__.wxapkg_decrypt_unpack/game.js",
  StartLine: 12000,
  EndLine: 12200
})
```

### 4. 分析和理解

阅读源码时重点关注：

- **类的继承关系**：extends 了哪个父类
- **属性定义**：有哪些成员变量及其类型
- **方法签名**：参数类型和返回值
- **核心逻辑**：关键的业务流程
- **依赖关系**：调用了哪些其他模块
- **配置使用**：如何读取和使用配置数据

### 5. 准确移植

基于源码实现进行移植时：

- **保持接口一致**：方法名、参数保持一致
- **保留核心逻辑**：关键的业务流程不要改变
- **适配项目差异**：根据项目规则调整（如横竖屏、Spine 替换等）
- **删除无关代码**：去除广告、运营活动等不需要的部分

### 6. 类型定义转换（JS → TypeScript）

⚠️ **重要提醒**：源码是 JavaScript，迁移到 TypeScript 项目时必须注意类型定义！

#### 核心原则

- **明确类型**：尽量为所有变量、参数、返回值定义明确的类型
- **避免 any**：除非确实无法确定类型，否则不要使用 `any`
- **类型推断**：利用 TypeScript 的类型推断能力，但关键接口必须显式声明

#### 类型定义策略

**属性类型定义**
```typescript
// ❌ 不好 - 没有类型
private equipData;
private position;

// ✅ 好 - 明确类型
private equipData: EquipData | null = null;
private position: { x: number; y: number } = { x: 0, y: 0 };
```

**方法参数和返回值**
```typescript
// ❌ 不好 - 参数和返回值类型不明确
init(data) {
  return this.process(data);
}

// ✅ 好 - 明确参数和返回值类型
init(data: EquipInitData): boolean {
  return this.process(data);
}
```

**配置数据类型**
```typescript
// ❌ 不好 - 使用 class
class EquipConfig {
  id: number;
  name: string;
}

// ✅ 好 - 使用 type 或 interface
export type EquipConfig = {
  id: number;
  name: string;
  attack?: number;  // 可选属性
  skills: number[];  // 数组类型
};
```

**数组和集合类型**
```typescript
// ❌ 不好 - 类型不明确
private items = [];
private map = {};

// ✅ 好 - 明确元素类型
private items: EquipItem[] = [];
private map: Map<number, EquipData> = new Map();
// 或使用对象字典
private dict: Record<number, EquipData> = {};
```

#### 从源码推断类型的方法

1. **查看赋值语句**
```javascript
// 源码中
this.speed = 5;
this.name = "brick";
this.isActive = true;

// 推断类型
private speed: number = 5;
private name: string = "brick";
private isActive: boolean = true;
```

2. **查看方法调用**
```javascript
// 源码中
this.setPosition(100, 200);
this.addItem({ id: 1, type: "weapon" });

// 推断签名
setPosition(x: number, y: number): void
addItem(item: { id: number; type: string }): void
```

3. **查看条件判断**
```javascript
// 源码中
if (data && data.equipList) {
  data.equipList.forEach(item => {
    // ...
  });
}

// 推断类型
type InitData = {
  equipList?: EquipItem[];  // 可选数组
};
```

4. **查看配置文件**
```javascript
// 源码中读取配置
const config = ConfigManager.getEquipConfig(id);
console.log(config.attack, config.defense);

// 参考 JSON 配置文件定义类型
export type EquipConfig = {
  id: number;
  attack: number;
  defense: number;
  // ... 其他字段
};
```

#### 常见类型定义模式

**事件处理器**
```typescript
private onMouseDown(e: Laya.Event): void {
  // ...
}
```

**回调函数**
```typescript
private onComplete: ((success: boolean) => void) | null = null;
```

**联合类型**
```typescript
type EquipType = "weapon" | "armor" | "accessory";
private equipType: EquipType;
```

**泛型使用**
```typescript
private getById<T>(id: number, list: T[]): T | undefined {
  return list.find(item => (item as any).id === id);
}
```

## 常见查找模式

### 查找类定义

```bash
# 搜索类定义
Query: "class ClassName"
# 或使用正则匹配
Query: "class\\s+ClassName\\s*(extends|\\{)"
IsRegex: true
```

### 查找方法实现

```bash
# 搜索方法定义
Query: "methodName\\s*\\("
IsRegex: true
```

### 查找属性使用

```bash
# 搜索属性访问
Query: "this.propertyName"
IsRegex: false
```

### 查找配置读取

```bash
# 搜索配置访问
Query: "ConfigManager" 或 "getConfig"
IsRegex: false
```

## 注意事项

### ⚠️ 源码特点

- 源码是压缩混淆后的代码，可读性较差
- 变量名可能被混淆，需要结合上下文理解
- 代码格式可能不规范，需要耐心分析

### ✅ 最佳实践

1. **先搜索后查看**：使用 grep_search 定位后再用 view_file 查看
2. **上下文分析**：查看足够的上下文代码（前后 50-100 行）
3. **交叉验证**：通过多个相关方法验证理解的正确性
4. **记录发现**：在代码注释中记录源码对应位置

### ❌ 避免的做法

1. **不要凭记忆实现**：即使之前看过，也要再次确认
2. **不要猜测行为**：不确定时必须查源码验证
3. **不要过度优化**：保持与源码逻辑一致，避免自作主张修改
4. **不要忽略细节**：看似不重要的代码可能有关键作用

## 示例场景

### 场景 1：移植 BrickEquip 类

**问题**：不确定 BrickEquip 的 init 方法参数类型

**步骤**：
1. 搜索 `class BrickEquip` 定位类定义
2. 搜索 `init\s*\(` 找到 init 方法
3. 查看方法实现，分析参数使用方式
4. 查看调用处，确认传入的数据结构

### 场景 2：实现拖拽逻辑

**问题**：不清楚拖拽流程的具体实现

**步骤**：
1. 搜索 `onMouseDown`、`onMouseMove`、`onMouseUp` 等事件处理
2. 查看 BagManager 中的拖拽相关方法
3. 分析 noEquipLayer 和 dragEquipLayer 的交互
4. 理解拖拽状态管理和位置计算逻辑

### 场景 3：适配配置数据

**问题**：不知道装备配置如何使用

**步骤**：
1. 搜索 `EquipConfig` 或配置相关的类名
2. 查看配置数据的读取方式
3. 分析配置字段在代码中的使用
4. 对照 JSON 配置文件定义 TypeScript 类型

## 工具推荐

- **grep_search**：快速定位目标代码
- **view_file**：查看具体实现
- **view_code_item**：查看类或方法定义（如果适用）

## 总结

遵循"源码参考优先"原则，可以：

✅ 确保移植的准确性和一致性  
✅ 避免因理解偏差导致的 bug  
✅ 减少反复修改的成本  
✅ 保持与原项目的兼容性  

**记住：当有任何疑问时，先查源码！**
