# makes it a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db= SQLAlchemy()
DB_NAME = "database.db"
ADMIN_CREATION_PASSWORD = "1234567" #TODO: Add to a config file

#blank function to create app

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hgbsdfbjh'
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .user.views import views
    from .user.auth import auth
    from .admin.auth_admin import auth_admin
    from .admin.views_admin import views_admin

    # url prefix says from where I can access the blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(auth_admin, url_prefix='/')
    app.register_blueprint(views_admin, url_prefix='/admin')

    from .models import User

    create_database(app=app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # get primary key (User here no specification of field needed )
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('created database!')
