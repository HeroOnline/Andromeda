#!/usr/bin/python3
# coding=utf-8


"""
工具类
"""


__author__ = 'LCD'


import sys
import os
import time
import datetime
import uuid
import platform


def cd_sys_type():
    """
    :return: 平台类型 0 win, 1 mac  2 Linux 3 其他
    """
    """
    a = sys.platform
    if a == 'win32' or a == 'win64':
        return 0
    elif a == 'darwin':
        return 1
    else:
        return 2
    """
    a = platform.system()
    if a == 'Windows':
        return 0
    elif a == 'Darwin':
        return 1
    elif a == 'Linux':
        return 2
    else:
        return 3


def cd_mac_uuid():
    """
    :return: 网卡作为设备号
    """
    return uuid.UUID(int=uuid.getnode()).hex[-12:]


def cd_mac_address():
    """
    :return: 网卡地址
    """
    mac = cd_mac_uuid()
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])


def cd_make_date_for_now(differ=30):
    """
    :param differ: 时间间隔
    :return:返回与当前时间相差 differ 天的日期
    """
    t = cd_time_now('%Y-%m-%d')
    t = datetime.datetime.strptime(t, '%Y-%m-%d')
    t += datetime.timedelta(days=+differ)
    return t.strftime('%Y-%m-%d')


def cd_make_date_list(d_start=None, d_end=None, join='-'):
    """
    :param d_start: 开始时间
    :param d_end: 结束时间
    :param join: 拼接符
    :return: 从开始至结束期间的日期表
    """
    strf = '%Y-%m-%d'
    if not d_start:
        d_start = '2016-01-01'
    if not d_end:
        d_end = datetime.datetime.now().strftime(strf)
    # 转为日期格式
    d_start = datetime.datetime.strptime(d_start, strf)
    d_end = datetime.datetime.strptime(d_end, strf)
    date_list = []
    # date_list = [cd_join_change(d_start.strftime(strf), '-', join)]
    while d_start < d_end:
        date_list.append(cd_join_change(d_start.strftime(strf), '-', join))  # 日期转字符串存入列表
        d_start += datetime.timedelta(days=+1)  # 日期叠加一天
    return date_list
    # print(date_list)


def cd_time_now(strftime="%Y-%m-%d %H:%M:%S"):
    """
    :param strftime: 时间格式 默认：%Y-%m-%d %H:%M:%S
    :return: 根据时间格式返回格式化当前时间
    """
    return time.strftime(strftime, time.localtime())


def cd_timestamp():
    """
    :return: 当前时间戳
    """
    return time.time()


def cd_time_to_timestamp(date, strftime="%Y-%m-%d %H:%M:%S"):
    """
    :param date: 时间来源
    :param strftime: 时间格式
    :return: 根据时间格式返回格式化输入时间date
    """
    return time.mktime(time.strptime(date,strftime))


def cd_timestamp_to_time(timestamp, strftime="%Y-%m-%d %H:%M:%S"):
    """
    :param timestamp: 时间戳
    :param strftime: 时间格式
    :return: 根据时间戳返回格式化时间
    """
    return time.strftime(strftime, time.localtime(timestamp))


def cd_join_change(s='', f='', t=''):
    """
    :param s:源字符串:
    :param f:原拼接符:
    :param t:拼接符:
    :return: 拼接后的字符串
    """
    arr = s.split(f)
    return t.join(arr)


def cd_sys_py_path():
    """
    获取当前文件路径
    :return: ~/cd_tools.py
    """
    return sys.argv[0]


def cd_file_py_path():
    """
    获取当前文件路径
    :return: ~/cd_tools.py
    """
    return __file__


def cd_os_path_cwd():
    """
    获取当前工作目录路径
    :return: ~/cd_tools.py
    """
    return os.getcwd()


def cd_os_path_abs():
    """
    获取当前工作目录路径
    :return:
    """
    return os.path.abspath('.')


def cd_os_path_abs_():
    """
    获取当前工作的  父目录  路径
    :return:
    """
    return os.path.abspath('..')


def cd_file_name(dir):
    """
    遍历 dir 目录下的所有文件
    :param dir: 需遍历的目录
    :return:
    """
    for root, dirs, files in os.walk(dir):
        print(root)
        print(dirs)
        print(files)


def cd_make_dirs(path):
    # os.chdir(path)
    # cd_make_dirs('archive_path')
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    '''
    print(platform.system())
    print(cd_mac_uuid())
    print(time.localtime())
    # print(cd_make_date_list('2019-08-27', '2019-11-27', '/'))
    a = cd_time_now()
    print(a)
    print(cd_timestamp())
    print(cd_time_to_timestamp(cd_timestamp_to_time(cd_timestamp(), "%Y-%m-%d"), "%Y-%m-%d"))
    # print(int(cd_time_to_timestamp('2018-11-11 00:00:00')))
    print(cd_make_date_list(cd_make_date_for_now(-30), cd_time_now('%Y-%m-%d'), '/'))
    print('------ 字符串大小 -----')
    s0 = '12:00'
    s1 = '12:00'
    s2 = '12:02'
    s3 = '11:59'
    s4 = '13:00'
    print(s0 == s1)
    print(s1>s2)
    print(s1>s3)
    print(s2>s4)
    t = cd_time_now('%Y-%m-%d %H:%M')
    print(type(t))
    print(cd_time_now('%Y-%m-%d %H:%M') + '.xls')
    '''


    list = os.listdir(os.path.abspath('..'))
    print(list)
    for name in list:
        print(name)
        if name.endswith('.xcodeproj'):
            print(name)
            print(True)

    # print(cd_sys_py_path())
    # print(cd_os_path_abs_for())
    # print(cd_os_path_abs_())
    # print(cd_make_dirs('c/testtt'))