#!/usr/bin/python3
# coding=utf-8


"""
提交ipa 到 fir.im
"""


__author__ = 'LCD'

import os


def upload_to_fir(path, fir_token):
    http_address = None
    if os.path.exists(path):
        ret = os.popen("fir p '%s' -T '%s'" % (path, fir_token))
        for info in ret.readlines():
            if "Published succeed" in info:
                http_address = info
                print(http_address)
                break
    else:
        print('')
    return http_address


def get_fir():
    """
    获取上传凭证 http://api.fir.im/apps
    :return:
    """
    pass


def get_fir():
    """
    获取上传凭证 http://api.fir.im/apps
    :return:
    """
    pass


def upload_to_fir_http():
    pass