import uuid
from datetime import datetime


class Place:
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, title=None, description=None, price=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price

        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
