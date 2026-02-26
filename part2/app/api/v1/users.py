#!/usr/bin/python3
"""
Users routes
"""

from flask import request, jsonify
from app.api.v1 import api_v1
from app.services.facade import facade


@api_v1.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user = facade.create_user(data)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@api_v1.route('/users', methods=['GET'])
def get_users():
    users = facade.get_users()
    return jsonify([user.to_dict() for user in users])


@api_v1.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = facade.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())


@api_v1.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = facade.update_user(user_id, data)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())
