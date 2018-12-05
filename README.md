# ![logo](https://github.com/liucaide/Andromeda/blob/master/imags/Andromeda.png)  Andromeda
iOS 持续集成方案，傻瓜式一键全自动化打包、上传工具！！！告别 fastlane 、Jenkins、Travis CI

![流程](https://github.com/liucaide/Andromeda/blob/master/imags/process%402x.png)
![配置](https://github.com/liucaide/Andromeda/blob/master/imags/plist.png)
## 使用方法
直接启动程序
☹️构建的Andromeda.app与debug时运行不一致，需在Python3环境下运行
~~- 1、将[app]()文件夹的 Andromeda.zip下载并解压。
- 2、将Andromeda文件夹 拖到 Application。
~~- 3、将 Xcode 内的 Applications 文件夹复制一份到 AndromedaPlist文件夹，并将 Application Loader.app 去除命名中空格重命名ApplicationLoader.app （/Applications/Xcode.app/Contents/Applications）原因见注意事项
- 4、按说明格式正确配置 Andromeda.plist 
~~- 5、启动 Andromeda.app

## 直接启动程序
```
python3 Andromeda.py
```
## HTTP 服务启动程序
调用说明:
```
// 通过浏览器内网访问
// target : 可填，项目 Target，对应plist中[root_info][Target]，填写则修改plist
// debug : 可填，bool值，项目构建环境 0 or 1，对应plist中[Target][debug]，填写则修改plist
 http://192.168.0.190:8989/ipa?target='TargetA'&debug=1
```

## 关于 Andromeda
## 注意事项
##### 关于上传至App Store 使用命令启动 Application Loader.app 内 altool的问题
> 1、由于 Xcode 内 的 Application Loader.app 命名中有空格，在命令执行打开的时候
会有错误 Application: No such file or directory，需将Application Loader.app中的空格去除 重命名 -> ApplicationLoader.app

> 2、为不影响Xcode内正常使用Application Loader.app（没验证，一般不会在Xcode内用），建议将Application Loader.app 所在 Applications文件夹复制到 Andromeda 配置文件夹 AndromedaPlist 内（或其他地方也行）并重命名Application Loader.app

> 3、在 Andromeda.plist 内正确输入 ApplicationLoader.app 地址

