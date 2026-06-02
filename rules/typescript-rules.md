---
trigger: always_on
---

# TypeScript 编码规范

本规则补充 TypeScript 命名、类型安全、产物体积与异步写法约定，与 `base-proj-rules.md` 等规则一并遵守。

---

## 一、命名规范

### 1.1 类（Class）

使用**大驼峰**（PascalCase）。

### 1.2 接口（Interface）

使用**大驼峰**（PascalCase）；**建议**以 `I` 作为前缀（如 `IUserData`），与具体类型区分。

### 1.3 方法（Method）与函数（Function）

使用**小驼峰**（camelCase）。

### 1.5 属性（Property）

- **公有**（`public`）：**小驼峰**（camelCase）。
- **私有 / 受保护**（`private` / `protected`）：以**下划线** `_` 开头，再接小驼峰（如 `_cache`、`_internalState`）。

### 1.6 常量（Constant）

使用**全大写 + 下划线分隔**，例如 `ECS_EVENT_STR`、`MAX_RETRY_COUNT`。

---

## 二、判空与安全

### 2.1 空安全

在运行环境支持的前提下，优先用 **Optional Chaining**（`?.`）与 **Nullish Coalescing**（`??`）简化判空与默认值，减少冗长 `if` 链。

---

## 三、类型与编译产物

### 3.1 仅类型的导出

为减少编译后 JS 体积，**仅作类型使用**的声明优先使用 `export type`，例如：

```typescript
export type Foo = { id: number };
```

避免在仅需类型处使用会生成运行时代码的写法（在适用场景下用 `import type` 配合）。

### 3.2 慎用 `any` 与宽泛 `object`

尽量减少 `any` 与过于宽泛的 `object`；若受第三方 API、遗留代码等限制**难以**收窄类型，须在对应处**写明注释**说明原因与预期形状或约束。

---

## 四、异步（Promise / async / await）

优先使用 **async / await** 与 **Promise** 组织异步逻辑。

**注意**：`await` 之后若结果可能为 `null` / `undefined`，**下一行使用前应做显式判空**（或与 `?.`、`??` 等组合），避免在未校验的情况下访问成员或调用方法。

---

## 五、与项目其他规则的关系

若与本仓库其他规则文件存在冲突，以**更严格或更贴近当前模块**的约定为准；无冲突时本文件与 `base-proj-rules.md`、AGENTS.md 等一并生效。
