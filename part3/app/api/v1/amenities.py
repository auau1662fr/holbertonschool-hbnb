from flask import request, jsonify
from app.api.v1 import api_v1
from app.services.facade import facade


@api_v1.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()

    amenity = facade.create_amenity(data)
    return jsonify(amenity.__dict__), 201


@api_v1.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = facade.get_amenities()
    return jsonify([a.__dict__ for a in amenities]), 200


@api_v1.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = facade.get_amenity(amenity_id)

    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404

    return jsonify(amenity.__dict__), 200


@api_v1.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    amenity = facade.get_amenity(amenity_id)

    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404

    for key, value in data.items():
        setattr(amenity, key, value)

    facade.amenity_repo.update()
    return jsonify(amenity.__dict__), 200
