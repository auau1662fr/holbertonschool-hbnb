from flask import request, jsonify
from app.api.v1 import api_v1

@api_v1.route('/amenities', methods=['GET'])
def get_amenities():
    return jsonify([])

@api_v1.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    return jsonify({"id": amenity_id})

@api_v1.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    return jsonify(data), 201

@api_v1.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    return jsonify({"id": amenity_id, "updated": data})
