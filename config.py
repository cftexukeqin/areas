#设置session所需的SECRET_KEY 每次登陆不一致
SECRET_KEY = 'fdsfjaskdljklda'

#自动加载模板
TEMPLATE_AUTO_RELOAD = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

#数据库连接配置
# HOSTNAME = '127.0.0.1'
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = ''
USERNAME = ''
PASSWORD = ''

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
# 判断初始化
INIT_FLAG = "true"