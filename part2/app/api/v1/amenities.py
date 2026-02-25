#!/usr/bin/python3
"""
Routes pour Amenity
"""

from flask import jsonify, request
from app.api.v1 import api_v1
from app.services.facade import facade


@api_v1.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = [a.to_dict() for a in facade.get_amenities()]
    return jsonify(amenities), 200


@api_v1.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    amenity = facade.create_amenity(data)
    return jsonify(amenity.to_dict()), 201


@api_v1.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = facade.get_amenity(amenity_id)
    if amenity:
        return jsonify(amenity.to_dict()), 200
    return jsonify({"error": "Amenity not found"}), 404


@api_v1.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    amenity = facade.update_amenity(amenity_id, data)
    if amenity:
        return jsonify(amenity.to_dict()), 200
    return jsonify({"error": "Amenity not found"}), 404


@api_v1.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    result = facade.delete_amenity(amenity_id)
    if result:
        return jsonify({"message": "Amenity deleted"}), 200
    return jsonify({"error": "Amenity not found"}), 404
