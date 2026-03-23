from app.persistence.sqlalchemy_repository import SQLAlchemyRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository()
        self.place_repo = SQLAlchemyRepository()
        self.review_repo = SQLAlchemyRepository()
        self.amenity_repo = SQLAlchemyRepository()

    # ================= USER =================

    def create_user(self, data):
        required_fields = ["first_name", "last_name", "email", "password"]

        missing = [f for f in required_fields if f not in data or not data[f]]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")

        user = User(**data)
        return self.user_repo.add(user)

    def get_users(self):
        return self.user_repo.get_all(User)

    def get_user(self, user_id):
        return self.user_repo.get(User, user_id)

    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if not user:
            return None

        for key, value in data.items():
            setattr(user, key, value)

        self.user_repo.update()
        return user

    # ================= PLACE =================

    def create_place(self, data):
        place = Place(**data)
        return self.place_repo.add(place)

    def get_places(self):
        return self.place_repo.get_all(Place)

    def get_place(self, place_id):
        return self.place_repo.get(Place, place_id)

    def update_place(self, place_id, data):
        place = self.get_place(place_id)
        if not place:
            return None

        for key, value in data.items():
            setattr(place, key, value)

        self.place_repo.update()
        return place

    # ================= REVIEW =================

    def create_review(self, data):
        review = Review(**data)
        return self.review_repo.add(review)

    def get_reviews(self):
        return self.review_repo.get_all(Review)

    def get_review(self, review_id):
        return self.review_repo.get(Review, review_id)

    def update_review(self, review_id, data):
        review = self.get_review(review_id)
        if not review:
            return None

        for key, value in data.items():
            setattr(review, key, value)

        self.review_repo.update()
        return review

    def delete_review(self, review_id):
        review = self.get_review(review_id)
        if not review:
            return None

        self.review_repo.delete(review)
        return True

    # ================= AMENITY =================

    def create_amenity(self, data):
        amenity = Amenity(**data)
        return self.amenity_repo.add(amenity)

    def get_amenities(self):
        return self.amenity_repo.get_all(Amenity)

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(Amenity, amenity_id)

    def update_amenity(self, amenity_id, data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None

        for key, value in data.items():
            setattr(amenity, key, value)

        self.amenity_repo.update()
        return amenity


# instance globale
facade = HBnBFacade()
