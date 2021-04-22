from flask import Flask
from app.bp_index import bp_index
from app.api import api
from app.login import login_manager, bp_login

def create_app(config_class='config.Developement'):
    app = Flask(__name__, static_folder='../web/static')
    app.config.from_object(config_class)

    # Blueprints
    app.register_blueprint(bp_index)
    app.register_blueprint(bp_login)

    #Init apps
    api.init_app(app)
    login_manager.init_app(app)

    return app