from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v1 import api_v1
from app.services.facade import facade


# ---------------- GET ALL ----------------
@api_v1.route('/places', methods=['GET'])
def get_places():
    places = facade.get_all_places()

    result = []
    for place in places:
        result.append({
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "owner_id": place.owner_id
        })

    return jsonify(result), 200


# ---------------- GET ONE ----------------
@api_v1.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = facade.get_place(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404

    return jsonify({
        "id": place.id,
        "title": place.title,
        "description": place.description,
        "price": place.price,
        "owner_id": place.owner_id
    }), 200


# ---------------- CREATE ----------------
@api_v1.route('/places', methods=['POST'])
@jwt_required()
def create_place():
    data = request.get_json()

    user_id = get_jwt_identity()

    if not data or "title" not in data:
        return jsonify({"error": "Missing data"}), 400

    place = facade.create_place({
        "title": data["title"],
        "description": data.get("description", ""),
        "price": data.get("price", 0),
        "owner_id": user_id
    })

    return jsonify({
        "id": place.id,
        "title": place.title
    }), 201


# ---------------- UPDATE ----------------
@api_v1.route('/places/<place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    data = request.get_json()
    user_id = get_jwt_identity()

    place = facade.get_place(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404

    # 🔥 sécurité : seul le propriétaire peut modifier
    if place.owner_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    if "title" in data:
        place.title = data["title"]

    if "description" in data:
        place.description = data["description"]

    if "price" in data:
        place.price = data["price"]

    facade.place_repo.update(place)

    return jsonify({"message": "Place updated"}), 200


# ---------------- DELETE ----------------
@api_v1.route('/places/<place_id>', methods=['DELETE'])
@jwt_required()
def delete_place(place_id):
    user_id = get_jwt_identity()

    place = facade.get_place(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404

    if place.owner_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    facade.place_repo.delete(place)

    return jsonify({"message": "Place deleted"}), 200
