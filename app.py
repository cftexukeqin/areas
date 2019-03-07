from flask import Flask
import config

from apps.front import bp
from exts import db,ma

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
ma.init_app(app)

# 蓝图注册
app.register_blueprint(bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
