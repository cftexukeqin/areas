#encoding:utf-8
from flask import jsonify


class HttpCode(object):
    default = 0
    ok = 200
    unautherror = 401
    paramserror = 1003
    servererrot = 500


def restful_result(code,message,data=None):
    return jsonify({'code':code,'message':message,'data':data or {}})

def success(message='',data=None):
    return restful_result(code=HttpCode.default,message=message,data=data)

def unauth_error(message=''):
    return restful_result(code=HttpCode.unautherror,message=message,data=None)

def params_error(message=''):
    return restful_result(code=HttpCode.paramserror,message=message,data=None)

def server_error(message=''):
    return restful_result(code=HttpCode.servererrot,message=message or '服务器内部错误',data=None)