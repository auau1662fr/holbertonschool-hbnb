
auau 1662 fr <auric.chen.2005@gmail.com>
10:18 (il y a 0 minute)
À moi

import uuid
from datetime import datetime
from app import db


class BaseModel(db.Model):
    """Base model for all tables"""
    __abstract__ = True

    id = db.Column(db.String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
