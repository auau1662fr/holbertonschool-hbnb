from flask import request, jsonify
from app.api.v1 import api_v1
from app.services.facade import facade


# 🔹 GET tous les users
@api_v1.route('/users', methods=['GET'])
def get_users():
    users = facade.get_all_users()
    return jsonify([u.to_dict() for u in users]), 200


# 🔹 GET user par id
@api_v1.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = facade.get_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict()), 200


# 🔹 CREATE user
@api_v1.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    required = ['first_name', 'last_name', 'email', 'password']
    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    user = facade.create_user(data)

    return jsonify(user.to_dict()), 201
