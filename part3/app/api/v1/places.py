from flask import request, jsonify
from app.api.v1 import api_v1
from app.services.facade import facade


@api_v1.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()

    place = facade.create_place(data)
    return jsonify(place.__dict__), 201


@api_v1.route('/places', methods=['GET'])
def get_places():
    places = facade.get_places()
    return jsonify([p.__dict__ for p in places]), 200


@api_v1.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = facade.get_place(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404

    return jsonify(place.__dict__), 200


@api_v1.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    place = facade.get_place(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404

    for key, value in data.items():
        setattr(place, key, value)

    facade.place_repo.update()
    return jsonify(place.__dict__), 200
