#!/usr/bin/python3
# coding=utf-8


"""
执行 Git 命令 监听新的提交 更新代码，
"""


__author__ = 'LCD'


import os
# from git import Repo




def pod_install(path, pod='install'):
    s = 'cd %s;' \
        'pod %s' \
        % (path, pod)
    ok = os.system(s)
    print ('---------->', ok)
    if ok > 0:
        raise Exception("pod %s Error !" % pod)
    else:
        pass


# if __name__ == '__main__':
#     path = '/Users/lcd/Desktop/TW/AUX_Bus'
#     pod_install(path, 'install')