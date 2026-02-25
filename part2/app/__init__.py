#!/usr/bin/python3
"""
Application factory
"""

from flask import Flask


def create_app():
    """
    Create and configure the Flask application
    """
    app = Flask(__name__)

    # Import and register API blueprint
    from app.api.v1 import api_v1
    app.register_blueprint(api_v1, url_prefix="/api/v1")

    return app
