#!/usr/bin/python3
"""
Routes pour Review
"""

from flask import jsonify, request
from app.api.v1 import api_v1
from app.services.facade import facade


@api_v1.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = [r.to_dict() for r in facade.get_reviews()]
    return jsonify(reviews), 200


@api_v1.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review = facade.create_review(data)
    return jsonify(review.to_dict()), 201


@api_v1.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = facade.get_review(review_id)
    if review:
        return jsonify(review.to_dict()), 200
    return jsonify({"error": "Review not found"}), 404


@api_v1.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = facade.update_review(review_id, data)
    if review:
        return jsonify(review.to_dict()), 200
    return jsonify({"error": "Review not found"}), 404


@api_v1.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    result = facade.delete_review(review_id)
    if result:
        return jsonify({"message": "Review deleted"}), 200
    return jsonify({"error": "Review not found"}), 404
