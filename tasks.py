#encoding:utf-8
from celery import Celery
from flask_mail import Message
from flask import Flask

import config
from utils.spider_data import Spider

app = Flask(__name__)
app.config.from_object(config)


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)


@celery.task
def spider_data():
    spider = Spider()
    spider.run()




