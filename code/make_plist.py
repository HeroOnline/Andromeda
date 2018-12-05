#!/usr/bin/python3
# coding=utf-8


"""
提交ipa 到 App Store
"""


__author__ = 'LCD'


import zipfile  # zip 解压
import plistlib  # plist 读写
import re  # 正则表达式操作


def read_plist_from_ipa(ipa_path):
    ipa = zipfile.ZipFile(ipa_path)

    plist_path = info_plist_path(ipa)

    plist_data = ipa.read(plist_path)

    plist_root = plistlib.loads(plist_data)

    print(plist_root)
    print('Display Name:', plist_root['CFBundleName'])
    print('Bundle Identifier:', plist_root['CFBundleIdentifier'])
    print('Version:', plist_root['CFBundleShortVersionString'])
    print('Bundle:', plist_root['CFBundleVersion'])

    return plist_root


def info_plist_path(zip_file):
    name_list = zip_file.namelist()
    pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
    for path in name_list:
        m = pattern.match(path)
        if m is not None:
            return m.group()


def read_plist(path):
    with open(path, 'rb') as fp:
        pi = plistlib.load(fp)
    # print(pi)
    return pi


def write_plist(path, obj):
    with open(path, 'wb') as fp:
        plistlib.dump(obj, fp)


# if __name__ == '__main__':
#     plist_path = '~/Desktop/MyWorking/Andromeda/code/Plist/Andromeda.plist'
#     obj = read_plist(plist_path)
#     obj['root_info']['ipa'] = ['abc', 'def']
#     write_plist(plist_path, obj)
