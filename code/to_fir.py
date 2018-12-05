#!/usr/bin/python3
# coding=utf-8


"""
提交ipa 到 fir.im
[文档](https://fir.im/docs/publish)
"""


__author__ = 'LCD'


import requests


# fir-cli 上传 不用此方法，减少配置fir-cli环境引发的问题
"""
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
"""


# http API 上传
class UploadToFir(object):

    def __init__(self, dic):
        print('---------->')
        print(dic)
        print('---------->')

        self.bundle_id = dic['bundle_id']
        self.api_token = dic['api_token']
        self.name = dic['name']
        self.version = dic['version']
        self.build = dic['build']
        self.type = dic['type']  # Adhoc | Inhouse
        self.changelog = dic['changelog']
        self.file = dic['file']
        self.binary = {}
        self.app_address = ''

    def get_fir_apps(self):
        """
        获取上传凭证 http://api.fir.im/apps
        :return:
        """
        try:
            r = requests.post('http://api.fir.im/apps', data={'type': 'ios',
                                                              'bundle_id': self.bundle_id,
                                                              'api_token': self.api_token})
        except:

            print('----- 获取上传凭证失败 -----')
            raise Exception("获取fir上传凭证失败 !")
        else:
            if r.status_code == 201:
                print(r.json()['cert']['binary'])
                self.app_address = 'https://fir.im/' + r.json()['short']
                self.binary = r.json()['cert']['binary']
                self.upload_fir()
            else:
                print('----- 获取上传凭证失败 ----->', r.status_code)
                raise Exception("获取fir上传凭证失败 !")

    def upload_fir(self):
        key = self.binary['key']
        token = self.binary['token']
        url = self.binary['upload_url']
        files = {'file':open(self.file, 'rb')}
        data = {'key': key,
                'token': token,
                'x:name': self.name,
                'x:version': self.version,
                'x:build': self.build,
                'x:release_type': self.type,
                'x:changelog': self.changelog,
                'file': self.file}
        try:
            print('----- 上传 fir ----->')
            r = requests.post(url, data=data, files=files)
        except:
            print('----- 上传 fir 失败 ----->')
            raise Exception("上传 fir 失败 !")
        else:
            if r.status_code == 200:
                print('-----上传 fir 完成----->', r)
            else:
                print('-----上传 fir 失败----->', r)
                raise Exception("上传 fir 失败 !")
            # print(r.json())
        finally:
            pass


# if __name__ == '__main__':
#     dic = {'bundle_id': '****',
#            'api_token': '****',
#            'name': '****',
#            'version': '1.0.7',
#            'build': '20180709010',
#            'type': 'Adhoc',
#            'changelog': '123',
#            'file': '~/Desktop/OIS/ipas/Debug/2018-11-27-14-02-23/IOS.ipa'}
#     t = UploadToFir(dic)
#     t.get_fir_apps()
#     # get_fir_apps(bundle_id, api_token)