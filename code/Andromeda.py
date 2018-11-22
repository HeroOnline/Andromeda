#!/usr/bin/python3
# coding=utf-8


"""
主程序入口

ipa 编译、打包
选择性上传 -> App Store  fir.im  蒲公英

附加：
UI操作窗口 -> 配置入口
监听 Git、SVN 更新、拉取到本地
http服务 远程 http 调起
"""


__author__ = 'LCD'


from ipa_build import *
from ui_input import TkSelect
from http_serve import *
from to_fir import *
from to_appstore import *
import json


def open_json_file():
    try:
        json_file = open("AutomationIpaInfo.json", 'r')
    except:
        return {}
    else:
        return read_json(json_file)


def read_json(json_file):
    try:
        dic = json.load(json_file)
    except:
        return {}
    else:
        return dic


def save_json(obj):
    d = json.dumps(obj, ensure_ascii=False)
    file = 'AutomationIpaInfo.json'
    json_file = open(file, 'w')
    json_file.write(d)
    json_file.close()


class Setup:
    def __init__(self):
        self.__tk()

    def __tk(self):
        dic = open_json_file()
        path = dic.get('path')
        plist = dic.get('plist')
        target = dic.get('target')
        is_workspace = dic.get('is_workspace') == 1
        is_release = dic.get('is_release') == 1
        is_http = dic.get('is_http')
        fir = dic.get('fir')
        s_name = dic.get('s_name')
        s_pwd = dic.get('s_pwd')

        select = TkSelect(660, 600,
                          path, plist,
                          target, bool(is_workspace),
                          bool(is_release), bool(is_http),
                          fir, s_name, s_pwd)
        select.source.subscribe(on_next=lambda value: self.ipa_build(value[0],
                                                                     value[1],
                                                                     value[2],
                                                                     value[3],
                                                                     value[4],
                                                                     value[5],
                                                                     value[6],
                                                                     value[7],
                                                                     value[8]))
        select.run()

    def ipa_build(self, path, plist, target, is_workspace, is_release, is_http, fir, s_name, s_pwd):
        """
        print('---------->')
        print(path)
        print(plist)
        print(target)
        print(is_workspace)
        print(is_release)
        print('---------->')
        """
        # Build(path, 'OIS', False, 'iPhone Distribution: Guangdong Erazar Information & Technology Co., Ltd. (774R9KNM5N)')

        dic = {'path': path,
               'plist': plist,
               'target': target,
               'is_workspace': int(is_workspace),
               'is_release': int(is_release),
               'fir': fir,
               's_name': s_name,
               's_pwd': s_pwd,
               }
        save_json(dic)
        print('---------->')
        print('dic:', dic)
        print('---------->')
        if is_http:
            http_source.subscribe(on_next=lambda value: self.archive(value))
            Serve(dic)
            # 通过浏览器访问局域网内 http://192.168.0.190:8989/ipa?debug=1&to=0
        else:
            self.archive(dic)

    def archive(self, dic):
        ipa = Archive(dic['path'], dic['plist'], dic['target'], bool(dic['is_workspace']), bool(dic['is_release']))

        if dic.get('fir'):
            ipa_path = ipa.ipa_path + '/' + ipa.target + '.ipa'
            upload_to_fir(ipa_path, dic.get('fir'))
        else:
            print('---------->')
            print('没有输入 Fir Token')
            print('---------->')

        if bool(dic['is_release']):
            if dic.get('s_name') and dic.get('s_pwd'):
                upload_to_appstore(ipa_path, dic.get('s_name'), dic.get('s_pwd'))
            else:
                print('---------->')
                print('没有输入 appstore 账号密码')
                print('---------->')

Setup()

"""
if __name__ == '__main__':
    Setup()
"""


