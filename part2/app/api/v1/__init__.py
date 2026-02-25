#!/usr/bin/python3
"""
API v1 blueprint
"""

from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

# Import routes AFTER blueprint creation
from app.api.v1.users import *
from app.api.v1.places import *
from app.api.v1.reviews import *
from app.api.v1.amenities import *
