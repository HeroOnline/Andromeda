#!/usr/bin/python3
# coding=utf-8


"""
提交ipa 到 蒲公英
[文档](https://www.pgyer.com/doc/api#uploadApp)
"""


__author__ = 'LCD'


import requests


pgy_url = 'https://qiniu-storage.pgyer.com/apiv1/app/upload'


def upload_to_pgyer(file, apikey, ukey, type=1, pwd='', des=''):

    files = {'file': open(file, 'rb')}
    data = {'_api_key': apikey,
            'uKey': ukey,
            'installType': type,        # (选填)应用安装方式，值为(1,2,3)。1：公开，2：密码安装，3：邀请安装。默认为1公开
            'password': pwd,           # (选填) 设置App安装密码，如果不想设置密码，请传空字符串，或不传。
            'updateDescription': des,  # (选填) 版本更新描述，请传空字符串，或不传。
            'file': file}
    # ssl._create_default_https_context = ssl._create_unverified_context
    try:
        print('----- 上传蒲公英 ----->')
        r = requests.post(pgy_url, data=data, files=files)
    except:
        print('----- 上传蒲公英失败 -----')
        raise Exception("上传蒲公英失败 !")
    else:
        if r.status_code == 200:
            print('-----上传蒲公英完成----->', r)
            return 'https://www.pgyer.com/' + r.json()['data']['appShortcutUrl']
        else:
            print('-----上传蒲公英失败----->', r)
            raise Exception("上传蒲公英失败 !")
        # print(r.json())
    finally:
        pass