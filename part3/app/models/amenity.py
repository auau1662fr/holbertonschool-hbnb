from app import db
from .base_model import BaseModel


class Amenity(BaseModel):
    """Amenity model"""

    __tablename__ = "amenities"

    name = db.Column(db.String(128), nullable=False)
