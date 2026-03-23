from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    from app.models import user, place, review, amenity

    from app.api.v1 import api_v1
    app.register_blueprint(api_v1, url_prefix="/api/v1")

    return app
