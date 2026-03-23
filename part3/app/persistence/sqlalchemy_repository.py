from app import db
class SQLAlchemyRepository:
    """Repository using SQLAlchemy for CRUD operations"""

    def add(self, obj):
        """Add an object to the database"""
        db.session.add(obj)
        db.session.commit()
        return obj

    def get(self, model, obj_id):
        """Get an object by ID"""
        return db.session.get(model, obj_id)

    def get_all(self, model):
        """Get all objects of a model"""
        return db.session.query(model).all()

    def update(self):
        """Commit changes"""
        db.session.commit()

    def delete(self, obj):
        """Delete an object"""
        db.session.delete(obj)
        db.session.commit()
