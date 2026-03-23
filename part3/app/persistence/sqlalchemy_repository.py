from app import db


class SQLAlchemyRepository:
    """Generic repository using SQLAlchemy"""

    def add(self, obj):
        """Add object to database"""
        db.session.add(obj)
        db.session.commit()
        return obj

    def get(self, model, obj_id):
        """Get object by id"""
        return model.query.get(obj_id)

    def get_all(self, model):
        """Get all objects of a model"""
        return model.query.all()

    def update(self):
        """Commit updates"""
        db.session.commit()

    def delete(self, obj):
        """Delete object"""
        db.session.delete(obj)
        db.session.commit()
