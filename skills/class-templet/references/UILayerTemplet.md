# UILayer 模板

## 功能
创建普通 UI 界面层类（全屏、半屏界面）。

## 继承关系
继承自 `UILayer` 基类。

## 代码模板

```typescript
import { Logger } from "@framework/utils/Logger";
import { UILayer } from "@logic/baseclass/ui/UILayer";
import { UIMng } from "@logic/manager/UIMng";
import { PkgName_CompName } from "@logic/uipara/FguiPara";
import { FguiCompName, FguiPkgName } from "@logic/uipara/UiNameTag";
import { TouchUtil } from "@logic/utils/touch/TouchUtil";
import * as fgui from "fairygui-cc";

/**
 * 界面：ClassName
 */
export class ClassName extends UILayer {
    // 组件引用
    protected uipara: PkgName_CompName = {};
    
    constructor() {
        super();
    }
    /**
     * 外部调用入口
     */
    static create(): void {
        const layer = new ClassName();
        layer.loadScene(FguiPkgName.PkgName, FguiCompName.CompName);
    }
    /**
     * 初始化界面 (组件绑定后调用)
     */
    public init(): void {
        super.init();
        this.initFgui();
        this.setData();
    }
    /**
     * 销毁
     */
    public dispose(): void {
        // 1. 清理自定义设置，引用类型、注册事件等
        // 
        // 2. 调用父类销毁（自动处理 fguiComp 和 uipara 清理）
        super.dispose();
    }
    /**
     * 网络协议响应
     * @param cmd 协议命令号
     */
    public netResponse(cmd: number): void {
        // 处理协议回调
        // switch(cmd) {
        //     case ProtoCmd.XXX:
        //         this.updateData();
        //         break;
        // }
    }
    /**
     * 初始化自定义设置
     */
    private initFgui(): void {
        // 1. 先设置 FGUI 扩展 (如有)，列表项渲染器或者独立组件需要设置扩展
        // this.setExtensionFgui("ui://包名/扩展组件名", 扩展组件类);
        // 2. 初始化列表项渲染器 (如有)
        // FguiUtil.setListItemRenderer(this.uipara.list_item, this, this.rendeItem,this.onRendeItem);
        // 3. 按钮点击示例
        // this.clickFgui(this.uipara.btn_close, this, this.onClick, ['btn_close'], true);
        // 4. 全局监听 (如有)，基类提供事件管理，无需手动管理
        // this.addBaseEvent(GlobalEvtEnum.xxx, this, this.xxx);
        // 5. 日志
        // Logger.log('这是测试日志，用于调试');
        // 6. 定时器 (如有)，基类提供定时器管理，无需手动管理
        // this.addBaseTimer(1000, -1, this, this.updateTimer);
    }
    /**
     * 设置数据
     */
    private setData(): void {

    }
    /**
     * 更新数据
     */
    private updateData(): void {

    }
    /**
     * 点击事件
     * @param btn 按钮
     */
    private onClick(btn: string): void {
        
    }
}
```

## 参数替换说明

- **ClassName**：大驼峰 (如 `Mail`)
- **PkgName**：全小写 (如 `mail`)
- **CompName**：大驼峰 (如 `Mail`)
- **PkgName_CompName**：组合格式 (如 `mail_Mail`)
