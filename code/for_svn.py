#!/usr/bin/python3
# coding=utf-8


"""
执行 SVN 命令 监听新的提交 更新代码，
"""


__author__ = 'LCD'


import os
# from git import Repo


def svn_update(path):
    s = 'cd %s;' \
        'svn update' \
        % (path)
    ok = os.system(s)
    print('---------->', ok)

    if ok > 0:
        if ok == 256:
            raise Exception("You need to upgrade the working copy first! Please see the 'svn upgrade' command")
        else:
            raise Exception("svn update Error !")
    else:
        pass

# if __name__ == '__main__':
#     path = '/Users/lcd/Desktop/TW/AUX_Bu'
#     svn_update(path)