from app import db
from .base_model import BaseModel


class Place(BaseModel):
    """Place model"""

    __tablename__ = "places"

    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    owner_id = db.Column(db.String(60), nullable=False)
