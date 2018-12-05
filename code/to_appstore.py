#!/usr/bin/python3
# coding=utf-8


"""
提交ipa 到 App Store
[文档](https://help.apple.com/itc/apploader/#/apdATD1E53-D1E1A1303-D1E53A1126)

由于 Xcode 内 的 Application Loader.app 命名中有空格，在命令执行打开的时候
会有错误 Application: No such file or directory，需将Application Loader.app中的空格去除
"""


__author__ = 'LCD'


import os


def upload_to_appstore(path, name, pwd, altool_path):
    print('----- 验证App----->')
    s = '%s ' \
        '--validate-app -f %s ' \
        '-u %s ' \
        '-p %s ' \
        '-t ios --output-format xml' % (altool_path, path, name, pwd)
    v = os.system(s)
    print('----------> ', v)
    if v == 0:
        print('----- 上传App----->')
        ss = '%s ' \
             '--upload-app -f %s  ' \
             '-u %s ' \
             '-p %s ' \
             '-t ios --output-format xml' % (altool_path, path, name, pwd)

        u = os.system(ss)
        if u == 0:
            print('----- 上传App 成功----->')
            pass
        else:
            raise Exception("上传 App Store 失败 !")
    else:
        raise Exception("验证 App 失败 !")


# if __name__ == '__main__':
#     path = '~/Desktop/OIS/ipas/Release/2018-11-29-11-44-35/OIS.ipa'
#     name = '*'
#     pwd = '*'
#     upload_to_appstore(path, name, pwd, altool_path)