from flask import request, jsonify
from app.api.v1 import api_v1
from app.services.facade import facade
from app.models.user import User


@api_v1.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    try:
        user = facade.create_user(data)
        return jsonify(user.__dict__), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api_v1.route('/users', methods=['GET'])
def get_users():
    users = facade.get_users()
    return jsonify([u.__dict__ for u in users]), 200


@api_v1.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = facade.get_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.__dict__), 200


@api_v1.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = facade.get_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    for key, value in data.items():
        setattr(user, key, value)

    facade.user_repo.update()
    return jsonify(user.__dict__), 200
