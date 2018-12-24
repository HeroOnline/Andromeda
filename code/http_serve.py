#!/usr/bin/python3
# coding=utf-8


"""
http访问入口  提供接口服务，可在浏览器访问调起
"""

__author__ = 'LCD'


from flask import Flask, request
import flask_restful
from cd_tools import *
import json
from build_manage import *


app = Flask(__name__)
api = flask_restful.Api(app)


def http_serve_value(tag, type):
    obj = read_andromeda_plist()
    if len(tag) > 0:
        dic = obj.get(tag)
        if dic:
            obj['root_info']['Target'] = tag

    if len(type) > 0:
        t = obj['root_info']['Target']
        obj[t]['ipaType'] = int(type)

    write_andromeda_plist(obj)
    launch_build()


class Http(flask_restful.Resource):
    def get(self, ipa):
        global http_source
        params = request.values
        target = ''
        type = ''
        if params.get('target'):
            target = params.get('target')
        if params.get('type'):
            type = params.get('type')

        try:
            http_serve_value(target, type)
            res = json.dumps('succeed', ensure_ascii=False)
        except Exception as e:
            res = json.dumps(e, ensure_ascii=False)
        finally:
            pass
        return res


api.add_resource(Http, '/<string:ipa>')

class Serve:
    def __init__(self):
        global app
        app.run(debug=False, port=8989, host='0.0.0.0')


# if __name__ == '__main__':
#     app.run(debug=False, port=8989, host='0.0.0.0')
#     # 通过浏览器访问 http://192.168.0.190:8989/ipa?target=''&type=1

