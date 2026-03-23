#!/usr/bin/python3
"""
HBnB Facade - Part 2 compliant
Only Review supports DELETE
"""

from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ================= USER =================

    def create_user(self, data):
        required_fields = ["first_name", "last_name", "email", "password"]

        missing_fields = [
            field for field in required_fields
            if field not in data or not data[field]
        ]

        if missing_fields:
            raise ValueError(
                f"Missing required fields: {', '.join(missing_fields)}"
            )

        user = User(**data)
        self.user_repo.add(user)
        return user

    def get_users(self):
        return self.user_repo.get_all()

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def update_user(self, user_id, data):
        return self.user_repo.update(user_id, data)


    # ================= PLACE =================

    def create_place(self, data):
        place = Place(**data)
        self.place_repo.add(place)
        return place

    def get_places(self):
        return self.place_repo.get_all()

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def update_place(self, place_id, data):
        return self.place_repo.update(place_id, data)


    # ================= REVIEW =================

    def create_review(self, data):
        review = Review(**data)
        self.review_repo.add(review)
        return review

    def get_reviews(self):
        return self.review_repo.get_all()

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def update_review(self, review_id, data):
        return self.review_repo.update(review_id, data)

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)


    # ================= AMENITY =================

    def create_amenity(self, data):
        amenity = Amenity(**data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenities(self):
        return self.amenity_repo.get_all()

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def update_amenity(self, amenity_id, data):
        return self.amenity_repo.update(amenity_id, data)


facade = HBnBFacade()
