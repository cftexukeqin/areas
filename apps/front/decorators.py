#encoding:utf-8
from flask import session
from functools import wraps
import config
from utils import restful

def init_check(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not config.INIT_FLAG in session:
            return func(*args,**kwargs)
        else:
            return restful.success(message="数据已经初始化")
    return wrapper