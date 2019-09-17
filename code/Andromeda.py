#!/usr/bin/python3
# coding=utf-8


"""
主程序入口

ipa 编译、打包
选择性上传 -> App Store  fir.im  蒲公英

附加：

监听 Git、SVN 更新、拉取到本地
http服务 远程 http 调起
"""


__author__ = 'LCD'


import os
from build_manage import *
from http_serve import *
import time
# 读取plist 文件
def setup():
    andromeda_plist = read_andromeda_plist()
    is_http = andromeda_plist['root_info']['Http_Serve']
    if is_http:
        http_serve()
    else:
        build_for_target()


# 查看ipa Target配置 —— 打包指定项目
def build_for_target():
    # 将此程序打包后 os.path 不能正确获得程序路径的情况，
    # pull_git() 版本管理尚未测试
    # pull_svn()
    launch_build()


# 查看是否启动 http 服务 —— 启动服务
def http_serve():
    """
    通过浏览器访问局域网内 http://192.168.0.190:8989/ipa?target=''&type=3&pod=install
    target(可选) 项目Target
    type(可选) 参数 构建 的IPA类型 0:appstore / 1:adhoc / 2:enterprise / 3:development
    pod (可选) 执行pod 指令  install  update   update MJRefresh ....
    :return:
    """
    Serve()




# info_t = """
# 第一次启动，需要按说明格式正确配置 Andromeda.plist，
# 并在下面输入 Andromeda.plist 存放路径👇
# """
# print(info_t)

#setup()

def build_1():
    http_serve_value('TargetA', '1')


def build_2():
    http_serve_value('TargetB', '1')

def build_3():
    http_serve_value('TargetA', '1')
    http_serve_value('TargetB', '1')



def build():
    print("""
        流程包括如下
        1：App -> 蒲公英：
        2：App -> 蒲公英：
        3：App+App -> 蒲公英：
        4：App -> App Store：（ ！！请检查代码完整性与版本号 ！！）
        5：App -> App Store：（ ！！请检查代码完整性与版本号 ！！）
        6：App+App -> App Store：（ ！！请检查代码完整性与版本号 ！！）
        888：全部流程 App+App -> 蒲公英 + App Store
        """)

    enums = input("请选择你需要执行的流程：1/2/3/4/5/6/7 ：")
    try:
        st = cd_timestamp()
        if enums == '1':
            build_1()
        elif enums == '2':
            build_2()
        elif enums == '3':
            build_3()
        et = cd_timestamp()
        print('用时：', int((et - st) / 60), '分钟')
    except Exception as e:
        print(e)
        build()
    else:
        print
        '已完成'
        next = input("是否继续构建(Y/N)：")
        if next == "Y" or next == "y":
            build()


if __name__ == '__main__':
    build()


