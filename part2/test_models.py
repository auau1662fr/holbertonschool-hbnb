#!/usr/bin/python3
"""
Test des modèles HBnB – Partie 2
"""

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

print("=== Testing User ===")
user = User(first_name="John", last_name="Doe", email="john@example.com", password="1234")
print(user.to_dict())
user.update(first_name="Jane", email="jane@example.com")
print("After update:", user.to_dict(), "\n")

print("=== Testing Place ===")
place = Place(title="Cozy Cottage", description="Nice place", price=100.0, latitude=45.0, longitude=-73.0, owner_id=user.id)
print(place.to_dict())
place.update(title="Luxury Cottage", price=150.0)
print("After update:", place.to_dict(), "\n")

print("=== Testing Review ===")
review = Review(user_id=user.id, place_id=place.id, rating=5, comment="Great stay!")
print(review.to_dict())
review.update(rating=4, comment="Good stay")
print("After update:", review.to_dict(), "\n")

print("=== Testing Amenity ===")
amenity = Amenity(name="Wi-Fi", description="High-speed internet")
print(amenity.to_dict())
amenity.update(description="Fiber-optic internet")
print("After update:", amenity.to_dict(), "\n")

print("All model tests completed ✅")
