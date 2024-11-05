# makes it a python package
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hgbsdfbjh'

    from views import views
    from auth import auth

    # url prefix says from where I can access the blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


