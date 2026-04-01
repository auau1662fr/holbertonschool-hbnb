from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Import des routes
from app.api.v1 import users
from app.api.v1 import places
from app.api.v1 import reviews
from app.api.v1 import amenities
from app.api.v1 import auth
