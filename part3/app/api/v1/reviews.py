from flask import request, jsonify
from app.api.v1 import api_v1
from app.services.facade import facade


@api_v1.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()

    review = facade.create_review(data)
    return jsonify(review.__dict__), 201


@api_v1.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = facade.get_reviews()
    return jsonify([r.__dict__ for r in reviews]), 200


@api_v1.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = facade.get_review(review_id)

    if not review:
        return jsonify({"error": "Review not found"}), 404

    return jsonify(review.__dict__), 200


@api_v1.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = facade.get_review(review_id)

    if not review:
        return jsonify({"error": "Review not found"}), 404

    for key, value in data.items():
        setattr(review, key, value)

    facade.review_repo.update()
    return jsonify(review.__dict__), 200


@api_v1.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = facade.get_review(review_id)

    if not review:
        return jsonify({"error": "Review not found"}), 404

    facade.review_repo.delete(review)
    return jsonify({"message": "Deleted"}), 200
