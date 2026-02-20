from flask import flask


def create_app():
    app = Flask(__name__)

    from .views.route import api
    app.register_blueprint(api)

    return app