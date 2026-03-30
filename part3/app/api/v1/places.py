from flask import request, jsonify
from app.api.v1 import api_v1

@api_v1.route('/places', methods=['GET'])
def get_places():
    return jsonify([])

@api_v1.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    return jsonify({"id": place_id})

@api_v1.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    return jsonify(data), 201

@api_v1.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    return jsonify({"id": place_id, "updated": data})
