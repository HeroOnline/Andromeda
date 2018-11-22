#!/usr/bin/python3
# coding=utf-8


"""
http访问入口  提供接口服务，可在浏览器访问调起
"""

__author__ = 'LCD'


from flask import Flask,request
import flask_restful
from cd_tools import *
import json
from rx.subjects import Subject

app = Flask(__name__)
api = flask_restful.Api(app)
http_source = Subject()
info = {}

class Http(flask_restful.Resource):
    def get(self, ipa):
        global info
        params = request.values
        debug = params.get('debug')
        if debug:
            info['is_release'] = False
            plist = info['plist']
            list = plist.split('/')
            a = list.pop()
            list.append('ipaAdHoc.plist')
            t = '/'
            plist = t.join(list)
            info['plist'] = plist
        else:
            info['is_release'] = True
            plist = info['plist']
            list = plist.split('/')
            a = list.pop()
            list.append('ipaAppStore.plist')
            t = '/'
            plist = t.join(list)
            info['plist'] = plist
        http_source.on_next(info)
        res = json.dumps('succeed', ensure_ascii=False)
        return res


api.add_resource(Http, '/<string:ipa>')


class Serve:
    def __init__(self, dic):
        global app
        global info
        info = dic
        app.run(debug=False, port=8989, host='0.0.0.0')


if __name__ == '__main__':
    app.run(debug=False, port=8989, host='0.0.0.0')
    # 通过浏览器访问 http://192.168.0.190:8989/ipa?debug=1

