from flask import request,redirect,render_template,jsonify,g,session
from sqlalchemy import or_
from sqlalchemy.orm import aliased


import config
from flask import Blueprint
from apps.front.models import AreasModel,area_schema,areas_schema,AreaSchema
from utils import restful
from utils.spider_data import Spider
from utils import dxcache
from .decorators import init_check
from exts import db

areamodel1 = aliased(AreasModel)
areamodel2 = aliased(AreasModel)


bp = Blueprint('front',__name__,url_prefix='')

"""
1、数据初始化
路径：/initialize
方式：GET
功能：首次从数据源抓取数据，如再次运行则提示已初始化
采用数据：2018年2月中华人民共和国县以上行政区划代码
返回数据-初始化成功："""

# 通过装饰器和session配合使用,判断初始化函数是否是第一次运行


@bp.route('/initialize')
@init_check
def spiderdata():
    spider = Spider()
    spider.run()
    count = AreasModel.query.count()
    data = {
        'num': count
    }
    session[config.INIT_FLAG] = 'dxsss'
    return restful.restful_result(code=0,message='Success',data=data)


"""
路径：/update
方式：GET
功能：从数据源查找是否有新的数据，如有则更新，如则提示
返回数据-更新成功："""


@bp.route("/update")
def update():
    old_count = AreasModel.query.count()
    all_infos = AreasModel.query.all()
    spider = Spider()
    if spider.check_update():
        # for info in all_infos:
        #     db.session.delete(info)
        #     db.session.commit()
        spider.run()
        update_url = spider.url
        new_count = AreasModel.query.count()
        update_num = new_count - old_count
        data = {
            'number':update_num,
            'url':update_url
        }
        return restful.success(message='数据更新成功',data=data)
    else:
        return restful.restful_result(code=1002,message="暂无新数据")


"""
路径：/query
方式：GET
功能：根据条件进行区域数据查询，返回结果
请求参数："""

@bp.route('/query',methods=['GET'])
def query():
    if request.method == "GET":
        q = request.args.get('id')
        depth = request.args.get('depth')
        keyword = request.args.get('keyword')
        area = None
        if depth == 1:
            area = AreasModel.query.filter(or_(AreasModel.id == q,AreasModel.name==keyword)).all()
        elif depth == 2:
            area = AreasModel.query.innerjoin(AreasModel).filter(areamodel1.id==areamodel2.pid).all()
        if area:
            result = areas_schema.dump(area).data
            return restful.success(message="查询成功",data=result)
        else:
            return restful.params_error(message="请输入查询条件")
    else:
        return restful.restful_result(code=405,message="不支持POST方法!")


@bp.route('/clear')
def clear_session():
    session.clear()
    return "Session 已经清除!"

