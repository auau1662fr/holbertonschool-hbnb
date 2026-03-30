from flask import request, jsonify
from app.api.v1 import api_v1
from app.services.facade import facade
from app.models.user import User

@api_v1.route('/users', methods=['GET'])
def get_users():
    return jsonify([])

@api_v1.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({"id": user_id})

@api_v1.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

@api_v1.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return jsonify({"id": user_id, "updated": data})
