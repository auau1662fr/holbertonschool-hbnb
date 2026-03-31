from flask import Flask
from app.extensions import db, bcrypt

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hbnb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)

    from app.api.v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    return app
