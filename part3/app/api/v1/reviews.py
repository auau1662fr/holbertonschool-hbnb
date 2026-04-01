from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v1 import api_v1
from app.services.facade import facade


# ---------------- GET ALL ----------------
@api_v1.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = facade.get_all_reviews()

    result = []
    for review in reviews:
        result.append({
            "id": review.id,
            "text": review.text,
            "rating": review.rating,
            "user_id": review.user_id,
            "place_id": review.place_id
        })

    return jsonify(result), 200


# ---------------- GET ONE ----------------
@api_v1.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = facade.get_review(review_id)

    if not review:
        return jsonify({"error": "Review not found"}), 404

    return jsonify({
        "id": review.id,
        "text": review.text,
        "rating": review.rating,
        "user_id": review.user_id,
        "place_id": review.place_id
    }), 200


# ---------------- CREATE ----------------
@api_v1.route('/reviews', methods=['POST'])
@jwt_required()
def create_review():
    data = request.get_json()
    user_id = get_jwt_identity()

    if not data or "text" not in data or "place_id" not in data:
        return jsonify({"error": "Missing data"}), 400

    place = facade.get_place(data["place_id"])

    if not place:
        return jsonify({"error": "Place not found"}), 404

    # 🔥 règle 1 : interdit review son propre place
    if place.owner_id == user_id:
        return jsonify({"error": "You cannot review your own place"}), 403

    # 🔥 règle 2 : pas de double review
    existing_reviews = facade.get_all_reviews()

    for review in existing_reviews:
        if review.user_id == user_id and review.place_id == data["place_id"]:
            return jsonify({"error": "You already reviewed this place"}), 400

    review = facade.create_review({
        "text": data["text"],
        "rating": data.get("rating", 0),
        "user_id": user_id,
        "place_id": data["place_id"]
    })

    return jsonify({
        "id": review.id,
        "text": review.text
    }), 201


# ---------------- UPDATE ----------------
@api_v1.route('/reviews/<review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    data = request.get_json()
    user_id = get_jwt_identity()

    review = facade.get_review(review_id)

    if not review:
        return jsonify({"error": "Review not found"}), 404

    # 🔐 seul le créateur peut modifier
    if review.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    if "text" in data:
        review.text = data["text"]

    if "rating" in data:
        review.rating = data["rating"]

    facade.review_repo.update(review)

    return jsonify({"message": "Review updated"}), 200


# ---------------- DELETE ----------------
@api_v1.route('/reviews/<review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    user_id = get_jwt_identity()

    review = facade.get_review(review_id)

    if not review:
        return jsonify({"error": "Review not found"}), 404

    if review.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    facade.review_repo.delete(review)

    return jsonify({"message": "Review deleted"}), 200
