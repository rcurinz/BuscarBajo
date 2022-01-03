from flask_script import Manager
from flask_migrate import Migrate
from exts import db
from app import app

manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db')

if __name__ == '__main__':
    manage.run()