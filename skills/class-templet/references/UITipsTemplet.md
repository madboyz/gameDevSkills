# UITips 模板

## 功能
创建弹窗 UI 界面层类（二次确认、奖励获得、通用提示）。

## 继承关系
继承自 `UITips` 基类。

## 代码模板

```typescript
import { Logger } from "@framework/utils/Logger";
import { UINodeLy } from "@gamestart/UINodeLy";
import { UITips } from "@logic/baseclass/ui/UITips";
import { UIMng } from '@logic/manager/UIMng';
import { PkgName_CompName } from "@logic/uipara/FguiPara";
import { FguiCompName, FguiPkgName } from "@logic/uipara/UiNameTag";
import { TouchUtil } from "@logic/utils/touch/TouchUtil";
import * as fgui from "fairygui-cc";

/**
 * 弹窗：ClassName
 */
export class ClassName extends UITips {
    protected uipara: PkgName_CompName = {};
    
    constructor() {
        super();
    }
    /**
     * 外部调用入口
     */
    static create(): ClassName {
        const layer = new ClassName();
        layer.loadScene(FguiPkgName.PkgName, FguiCompName.CompName);
        return layer;
    }
    /**
     * 初始化界面
     */
    public init(): void {
        super.init();
        // 设置挂靠的节点层级 (默认为 tipLayer)
        this.setParent(UINodeLy.tipLayer);
        // 弹窗通常需要遮罩处理
        UIMng.i.halfScreenMask(false, true);
        this.initFgui();
        this.setData();
    }
    /**
     * 销毁
     */
    public dispose(): void {
        super.dispose();
        // 恢复遮罩状态
        UIMng.i.halfScreenMask(true, true);
    }
    /**
     * 初始化自定义设置
     */
    private initFgui(): void {
        // 按钮监听示例
        // this.clickFgui(this.uipara.btn_confirm, this, this.onClick, ['btn_confirm'], true);
    }
    /**
     * 设置数据
     */
    public setData(): void {

    }
    /**
     * 点击事件处理
     * @param btn 按钮名称
     */
    private onClick(btn: string): void {

    }
    /**
     * 点击空白区域返回
     */
    protected clickBlankBack()
    {
        Logger.log('clickBlankBack');
    }
}
```

## 参数替换说明

- **ClassName**：大驼峰 (如 `MailTips`)
- **PkgName**：全小写 (如 `mail`)
- **CompName**：大驼峰 (如 `MailTips`)
- **PkgName_CompName**：组合格式 (如 `mail_MailTips`)
