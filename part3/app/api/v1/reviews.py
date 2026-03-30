from flask import request, jsonify
from app.api.v1 import api_v1
from app.services.facade import facade


@api_v1.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify([])

@api_v1.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    return jsonify({"id": review_id})

@api_v1.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    return jsonify(data), 201

@api_v1.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    return jsonify({"id": review_id, "updated": data})

@api_v1.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    return jsonify({"deleted": review_id})
