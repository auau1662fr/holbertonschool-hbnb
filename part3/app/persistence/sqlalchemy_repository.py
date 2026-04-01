from app.extensions import db


class SQLAlchemyRepository:
    def __init__(self, model):
        self.model = model

    # ---------------- CREATE ----------------
    def add(self, obj):
        db.session.add(obj)
        db.session.commit()
        return obj

    # ---------------- READ ----------------
    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def get_by_attribute(self, attr, value):
        return self.model.query.filter(
            getattr(self.model, attr) == value
        ).first()

    # ---------------- UPDATE ----------------
    def update(self, obj):
        db.session.commit()
        return obj

    # ---------------- DELETE ----------------
    def delete(self, obj):
        db.session.delete(obj)
        db.session.commit()
        return True
