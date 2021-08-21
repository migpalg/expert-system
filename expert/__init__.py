import os
from . import blueprints
from flask import Flask


def create_app(test_config=None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(blueprints.questions)

    return app
