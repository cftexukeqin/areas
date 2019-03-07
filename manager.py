from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate

from exts import db
from app import app
from apps.front.models import AreasModel


manager = Manager(app)

migrate = Migrate(app,db,compare_type=True)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()