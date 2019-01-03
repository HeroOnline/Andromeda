#!/usr/bin/python3
# coding=utf-8


"""
执行 Git 命令 监听新的提交 更新代码，
"""


__author__ = 'LCD'


import os
# from git import Repo


def read_git_log(path):
    s = 'cd %s;' \
        'git log --oneline' \
        % (path)
    os.system(s)


def git_pull(path):
    s = 'cd %s;' \
        'git pull' \
        % (path)
    ok = os.system(s)
    print('---------->', ok)
    if ok > 0:
        raise Exception("git pull Error !")
    else:
        pass


# if __name__ == '__main__':
#     path = '/Users/lcd/Desktop/MyWorking/CDKit/Andromeda'
#     git_pull(path)