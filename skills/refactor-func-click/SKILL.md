---
name: refactor-func-click
description: Automates the refactoring of LayaAir TypeScript files to comply with the 'require-func-click' ESLint rule by replacing direct event binding with Func.AddClick/RemoveClick.
---

# Refactor Func Click

This skill automates the refactoring process to enforce the `require-func-click` ESLint rule. It scans TypeScript files for direct usages of `Laya.Event.CLICK` or `MouseEvent.CLICK` (via `.on`, `.once`, or `.off`) and replaces them with the standardized `Func.AddClick` and `Func.RemoveClick` wrappers.

## Usage

Run the provided Python script to scan the `src` directory and apply fixes automatically.

```bash
python .trae/skills/refactor-func-click/scripts/refactor.py
```

## Transformation Rules

1.  **Registration (`on`/`once`)**:
    *   **Pattern**: `obj.on(Laya.Event.CLICK|MouseEvent.CLICK, caller, listener, [args])`
    *   **Replacement**: `Func.AddClick(obj, caller, listener, [args])`
    *   *Note*: Supports complex object paths and array access (e.g., `this.tabVec[i]`).
    *   *Note*: `once` is also replaced by `AddClick`. Verify behavior if single-shot click is strictly required.
    *   *Note*: To force `downScale = false`, add a comment `// downScale=false` on the same line as the `.on` call.
        *   Example: `btn.on(..., ...); // downScale=false` -> `Func.AddClick(..., ..., ..., null, false);`
    *   *Note*: Existing `Func.AddClick` calls are preserved and not modified.

2.  **Removal (`off`)**:
    *   **Pattern**: `obj.off(Laya.Event.CLICK|MouseEvent.CLICK, caller, listener)`
    *   **Replacement**: `Func.RemoveClick(obj)`

3.  **Imports**:
    *   Automatically adds `import { Func } from "...";` if missing, calculating the correct relative path.

## Exclusions

*   `src/script/common/Func.ts` is excluded from processing.

## Verification

After running the refactoring script, verify the build using:

```bash
esbuild src/Main.ts --bundle --sourcemap --watch --charset=utf8 --platform=browser --target=es6 --outfile=bin/js/bundle.js
```
