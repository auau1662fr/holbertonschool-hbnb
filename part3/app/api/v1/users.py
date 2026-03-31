from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User

users_bp = Blueprint('users', __name__)

# GET all users
@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


# GET one user
@users_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200


# CREATE user
@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    required = ["first_name", "last_name", "email", "password"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    user = User(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email")
    )

    # HASH PASSWORD
    user.set_password(data.get("password"))

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201
