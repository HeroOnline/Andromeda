#!/usr/bin/python3
# coding=utf-8


"""
主程序入口

ipa 编译、打包
选择性上传 -> App Store  fir.im  蒲公英

附加：

监听 Git、SVN 更新、拉取到本地
http服务 远程 http 调起
"""


__author__ = 'LCD'


import os
from make_plist import *
from ipa_build import *
from to_fir import *
from to_appstore import *
from to_pgyer import *
from send_email import *

plist_path = 'Andromeda/Andromeda.plist'
info_plist = {}
build_tag = ''
is_debug = True
plist_path_adhoc = ''
plist_path_appstore = ''


# 读取plist 文件
def read_andromeda_plist():
    global plist_path
    """
    try:
        f = open('andromeda.txt', 'r')
    except:
        str = input('请输入Andromeda.plist 路径：')
        with open('andromeda.txt', 'w') as f:
            f.write(str)
            f.close()
        plist_path = str
    else:
        str = f.read()
        plist_path = str
        f.close()
    finally:
        pass
    """
    return read_plist(plist_path)

# 读取plist 文件
def write_andromeda_plist(obj):
    write_plist(plist_path, obj)


def launch_build():
    global info_plist
    global build_tag
    global plist_path_adhoc
    global plist_path_appstore
    global is_debug
    info_plist = read_andromeda_plist()
    plist_path_adhoc = info_plist['root_info']['Path_ipa_plist'] + '/ipaAdHoc.plist'
    plist_path_appstore = info_plist['root_info']['Path_ipa_plist'] + '/ipaAppStore.plist'
    build_tag = info_plist['root_info']['Target']
    is_debug = info_plist[build_tag]['debug']
    build_ipa()

def build_ipa():
    global is_debug
    global plist_path_adhoc
    global plist_path_appstore
    info = info_plist[build_tag]
    buidPlist_path = plist_path_adhoc if is_debug else plist_path_appstore
    xc_path = info['xc_path']
    is_workspace = xc_path.endswith('.xcworkspace')
    t = '/'
    list = xc_path.split('/')
    list.pop()
    main_path = t.join(list)

    try:
        ipa = Archive(main_path, buidPlist_path, build_tag, is_workspace, not is_debug)
    except Exception as e:
        print('---------->', e, '---------->')
    else:
        ipa_path = ipa.ipa_path + '/' + ipa.target + '.ipa'  # 打包好的IPA文件地址
        if os.path.exists(ipa_path):
            ipa_plist = read_plist_from_ipa(ipa_path)
            if is_debug:
                to_fir(ipa_path, ipa_plist)
                to_pgyer(ipa_path)
            else:
                to_app_store(ipa_path)
        else:
            print('----------> \n 错误，未检索到 ipa 文件,可能打包不成功 \n---------->')
    finally:
        pass


def to_fir(ipa_path, ipa_plist):
    info = info_plist[build_tag]['fir']
    if len(info['token']) > 0:
        dic = {'bundle_id': ipa_plist['CFBundleIdentifier'],
               'name': ipa_plist['CFBundleName'],
               'version': ipa_plist['CFBundleShortVersionString'],
               'build': ipa_plist['CFBundleVersion'],
               'api_token': info['token'],
               'type': info['type'],
               'changelog': '',
               'file': ipa_path}
        try:
            t = UploadToFir(dic)
        except Exception as e:
            pass
        else:
            try:
                t.get_fir_apps()
            except Exception as e:
                pass
            else:
                send_email(t.app_address)
            finally:
                pass
        finally:
            pass



def to_pgyer(ipa_path):
    info = info_plist[build_tag]['pgyer']
    if len(info['api_key']) > 0 and len(info['api_key']) > 0 :
        try:
            address = upload_to_pgyer(ipa_path,
                            info['api_key'],
                            info['user_key'],
                            info['type'],
                            info['password'],
                            '')

        except Exception as e:
            pass
        else:
            send_email(address)


def to_app_store(ipa_path):
    info = info_plist[build_tag]['app_store']
    altoo_path = info_plist['root_info']['Path_altool']
    if len(info['account']) > 0 and len(info['password']) > 0:
        try:
            upload_to_appstore(ipa_path, info['account'], info['password'], altoo_path)
        except Exception as e:
            print('---------->', e, '---------->')
        else:
            pass


def send_email(app_address):
    info = info_plist[build_tag]['notification']
    if len(info['email_from_name']) > 0 \
            and len(info['email_from_pwd']) > 0 \
            and len(info['email_smtp']) > 0 \
            and len(info['email_to']) > 0:
        email_send(info['email_from_name'],
                   info['email_from_pwd'],
                   info['email_to'],
                   info['email_smtp'],
                   app_address)