# ![logo](https://github.com/liucaide/Andromeda/blob/master/imags/Andromeda.png)  Andromeda
iOS 持续集成方案，傻瓜式一键全自动化打包、上传工具！！！告别 fastlane 、Jenkins（附加功能尚未完成）
> 前言：目前市面上iOS开发持续集成的方案很多，在主流的分发平台fir、蒲公英都有相应的方案介绍（fastlane，Jenkins）;但就实际需求来说还是不够友好，在前面使用Python为公司开发两个自动化脚本之余，产生使用Python开发一个完全傻瓜式的自动化脚本，并满足自身需求。
<img src="https://github.com/liucaide/Andromeda/blob/master/imags/process%402x.png" width="400" align=center />
<img src="https://github.com/liucaide/Andromeda/blob/master/imags/plist.jpeg" width="400" align=center />
## 需求来源
- 可运行脚本 或 集成App使用，傻瓜式运行
- 无需配置运行环境（Mac 自带Python 2.7）
- 随身携带，即插即用
- 满足跨平台打包唤起（http服务）
- 可唤起多个项目打包
- 自动执行 git / svn 命令更新代码
- 自动上传指定分发平台，包括App Store
- 上传完毕通知测试等相关人员（邮件、QQ、微信）
## 使用方法
#### 直接启动程序

☹️构建的Andromeda.app与Development时运行不一致，问题尚未明确

~~- 1、将[app]()文件夹的 Andromeda.zip下载并解压。~~

~~- 2、将Andromeda文件夹 拖到 Application，配置好Andromeda.plist，启动Andromeda.app即可~~

~~- 3、将 Xcode 内的 Applications 文件夹复制一份到 Andromeda文件夹，并将 Application Loader.app 去除命名中空格重命名ApplicationLoader.app （/Applications/Xcode.app/Contents/Applications）原因见注意事项~~

~~- 4、按说明格式正确配置 Andromeda.plist~~

~~- 5、启动 Andromeda.app~~

#### python 命令启动程序
```
python Andromeda.py // python2 暂不兼容
or
python3 Andromeda.py
```
#### HTTP服务启动程序
如果你使用另一台Mac打包，那么可以启用HTTP服务，只需调用接口即可启动整个流程
```
// 通过浏览器内网访问
/*
target(可选) 项目Target
type(可选) 参数 构建 的IPA类型 0:appstore / 1:adhoc / 2:enterprise / 3:development
*/
http://192.168.0.190:8989/ipa
or
http://192.168.0.190:8989/ipa?target='TargetA'&type=0
```

## 关于 Andromeda
## 注意事项
##### 关于上传至App Store 使用命令启动 Application Loader.app 内 altool的问题
> 1、由于 Xcode 内 的 Application Loader.app 命名中有空格，在命令执行打开的时候
会有错误 Application: No such file or directory，需将Application Loader.app中的空格去除 重命名 -> ApplicationLoader.app

> 2、为不影响Xcode内正常使用Application Loader.app（没验证，一般不会在Xcode内用），建议将Application Loader.app 所在 Applications文件夹复制到 Andromeda 配置文件夹 Andromeda 内（或其他地方也行）并重命名Application Loader.app

> 3、在 Andromeda.plist 内正确输入 ApplicationLoader.app 地址

