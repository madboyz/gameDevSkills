# Component 模板

## 功能
创建可复用的 UI 独立组件（列表项、公共单元块等）。

## 继承关系
继承自 `fgui.GComponent` 基类。

## 代码模板

```typescript
import { PkgName_CompName } from "@logic/uipara/FguiPara";
import { FguiUtil } from "@logic/utils/fgui/FguiUtil";
import * as fgui from "fairygui-cc";

/**
 * 业务名：ClassName
 */
export class ClassName extends fgui.GComponent {
    protected uipara: PkgName_CompName = {}!;

    constructor() {
        super();
    }
    /**
     * 构造函数 (由 FGUI 内部调用)
     */
    protected onConstruct(): void {
        // 绑定模块化界面参数
        FguiUtil.bindUipara(this, this.uipara);
        // 初始化自定义逻辑

    }
    /**
     * 销毁 (由 FGUI 内部调用)
     */
    public dispose(): void {
        // 清理引用、取消事件监听
        this.uipara = null;
        super.dispose();
    }
    /**
     * 设置数据
     * @param data 业务数据
     */
    public setData(data: any): void {

    }
}
```

## 参数替换说明

- **ClassName**：大驼峰 (如 `MailItem`)
- **PkgName**：全小写 (如 `mail`)
- **CompName**：大驼峰 (如 `MailItem`)
- **PkgName_CompName**：组合格式 (如 `mail_MailItem`)

