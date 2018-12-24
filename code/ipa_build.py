#!/usr/bin/python3
# coding=utf-8


"""
ipa 编译 打包
"""


__author__ = 'LCD'

import os
from cd_tools import *


"""
新版打包方式

"""


class Archive(object):
    def __init__(self, path, export_plist, target, is_workspace, type):
        """
        :param path: 项目文件夹路径
        :param export_plist: 打包配置文件
        :param target: 项目 target
        :param is_workspace: .xcworkspace or .xcodeproj
        :param type: 1--3 Debug or -0 Release
        """
        print('---------->')
        print('项目目录：', path)
        print('配置文件：', export_plist)
        print('target：', target)
        print('is_workspace：', is_workspace)
        print('build_type：', type)
        print('---------->')

        self.path = path
        self.export_plist = export_plist
        self.target = target

        self.archive_path = path + '/archives'
        time = cd_time_now()
        # time.replace(":", "-")
        arr = time.split(':')
        time = '-'.join(arr)
        arr = time.split(' ')
        time = '-'.join(arr)
        self.archive_name = target + '-' + time

        self.ipa_path = path + ('/ipas/Release/' if type == 0 else '/ipas/Debug/') + time

        self.is_workspace = is_workspace
        self.build_type = 'Release' if type == 0 else 'Debug'

        self.__clean()
        self.__build()
        self.__ipa()


    def __clean(self):
        clean = '-workspace %s.xcworkspace' % (self.target) if self.is_workspace else '-project %s.xcodeproj'%(self.target)
        s = 'cd %s;' \
            'xcodebuild clean %s ' \
            '-scheme %s ' \
            '-configuration %s' \
            % (self.path, clean, self.target, self.build_type)
        ok = os.system(s)
        if ok > 0:
            raise Exception("Clean Error !")
        else:
            pass


    def __build(self):
        build = "-workspace %s.xcworkspace" % self.target if self.is_workspace else "-project %s.xcodeproj" % self.target
        s = "cd %s;" \
            "xcodebuild archive %s " \
            "-scheme %s " \
            "-archivePath %s/%s " \
            % (self.path, build, self.target, self.archive_path, self.archive_name)
        ok = os.system(s)
        if ok > 0:
            raise Exception("Archive Error !")
        else:
            pass

    def __ipa(self):
        s = "cd %s;" \
            "xcodebuild -exportArchive -archivePath %s/%s.xcarchive" \
            " -exportPath %s" \
            " -exportOptionsPlist '%s'" \
            % (self.path, self.archive_path, self.archive_name, self.ipa_path, self.export_plist)
        print('----------> self.archive_path', self.archive_path)
        print('----------> self.archive_name', self.archive_name)
        print('----------> self.ipa_path', self.ipa_path)
        print('----------> self.export_plist', self.export_plist)
        ok = os.system(s)
        if ok > 0:
            raise Exception("Export Error !")
        else:
            pass


"""
旧版打包方式 8.3以下
注意事项，xcode Signing code 不能选择自动
必须配置 Debug  Release 环境 配置文件
"""
"""
class Build(object):

    def __init__(self, path, target, is_workspace, certificate):
        self.path = path
        self.target = target
        self.is_workspace = is_workspace
        self.certificate = certificate
        self.__clean()
        self.__build()
        self.__ipa()

    def __clean(self):
        if self.is_workspace:
            s = 'cd %s;' \
                'xcodebuild -workspace %s.xcworkspace' \
                ' -scheme %s clean' \
                % (self.path, self.target, self.target)
            os.system(s)
        else:
            s = 'cd %s;' \
                'xcodebuild -target %s clean' \
                % (self.path, self.target)
            os.system(s)

    def __build(self):

        if self.is_workspace:
            s = "cd %s;" \
                "xcodebuild -workspace %s.xcworkspace" \
                " -scheme %s" \
                " CODE_SIGN_IDENTITY='%s'" \
                " -derivedDataPath build/" \
                % (self.path, self.target, self.target, self.certificate)
            os.system(s)
        else:
            s = "cd %s;" \
                "xcodebuild -target %s" \
                " CODE_SIGN_IDENTITY='%s'"\
                % (self.path, self.target, self.certificate)
            os.system(s)

    def __ipa(self):
        s = "cd %s;" \
            "xcrun -sdk iphoneos PackageApplication -v %s" \
            "/build/Build/Products/Debug-iphoneos/%s.app -o %s/%s.ipa" \
            " CODE_SIGN_IDENTITY='%s'" \
            % (self.path, self.path, self.target, self.path, self.target, self.certificate)
        os.system(s)
"""
