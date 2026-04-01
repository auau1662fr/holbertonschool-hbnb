from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.api.v1 import api_v1
from app.services.facade import facade


@api_v1.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    user = facade.get_user_by_email(email)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not user.check_password(password):
        return jsonify({"error": "Wrong password"}), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({
        "access_token": access_token
    }), 200
