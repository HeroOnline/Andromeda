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
from for_git import *
from for_svn import *

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
    通过浏览器访问局域网内 http://192.168.0.190:8989/ipa?target=''&type=3
    target(可选) 项目Target
    type(可选) 参数 构建 的IPA类型 0:appstore / 1:adhoc / 2:enterprise / 3:development
    :return:
    """
    Serve()


def pull_git():
    andromeda_plist = read_andromeda_plist()
    tag = andromeda_plist['root_info']['Target']
    path = andromeda_plist[tag]['git']['git_path']
    if len(path) > 0:
        git_pull()

def pull_svn():
    andromeda_plist = read_andromeda_plist()
    tag = andromeda_plist['root_info']['Target']
    path = andromeda_plist[tag]['svn']['svn_path']
    if len(path) > 0:
        svn_update()

# info_t = """
# 第一次启动，需要按说明格式正确配置 Andromeda.plist，
# 并在下面输入 Andromeda.plist 存放路径👇
# """
# print(info_t)

setup()

# if __name__ == '__main__':
#     setup()


