from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

from app.persistence.sqlalchemy_repository import SQLAlchemyRepository


class Facade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

    # ---------------- USERS ----------------

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    def create_user(self, data):
        user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            is_admin=data.get("is_admin", False)
        )
        user.set_password(data["password"])
        self.user_repo.add(user)
        return user

    def update_user(self, user_id, data):
        user = self.user_repo.get(user_id)
        if not user:
            return None

        for key, value in data.items():
            if key == "password":
                user.set_password(value)
            elif hasattr(user, key):
                setattr(user, key, value)

        self.user_repo.update(user)
        return user

    def delete_user(self, user_id):
        user = self.user_repo.get(user_id)
        if not user:
            return False

        self.user_repo.delete(user)
        return True

    # ---------------- PLACES ----------------

    def get_all_places(self):
        return self.place_repo.get_all()

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def create_place(self, data):
        place = Place(**data)
        self.place_repo.add(place)
        return place

    # ---------------- REVIEWS ----------------

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def create_review(self, data):
        review = Review(**data)
        self.review_repo.add(review)
        return review

    # ---------------- AMENITIES ----------------

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def create_amenity(self, data):
        amenity = Amenity(**data)
        self.amenity_repo.add(amenity)
        return amenity


# 🔥 instance globale
facade = Facade()
