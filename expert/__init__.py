from . import blueprints
from flask import Flask
from flask_cors import CORS


def create_app(test_config=None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(blueprints.questions)
    app.register_blueprint(blueprints.careers)

    return app
