from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

from app.api.v1.users import users_bp

api_v1.register_blueprint(users_bp)
