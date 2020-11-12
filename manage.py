#-*-coding:utf-8-*-
from flask_script import Manager
from App import app
from flask_migrate import Migrate,MigrateCommand
from extension import db
from models import *

manage = Manager(app)
migrate = Migrate(app,db)

# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade

manage.add_command('db',MigrateCommand)

if __name__=='__main__':
    manage.run()
