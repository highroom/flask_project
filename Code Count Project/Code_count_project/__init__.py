from flask import Flask
from .views.account import account
from .views.index import ind


def create_app():
    app = Flask(__name__)
    # 从settings文件下的Config类读取配置信息
    app.config.from_object('settings.Config')
    app.register_blueprint(account)
    app.register_blueprint(ind)
    return app
