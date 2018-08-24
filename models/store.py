"""Store Model definition."""
from db import db


class StoreModel(db.Model):
    """Store Model class definition."""

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel',
                            lazy='dynamic',
                            back_populates='store')

    def __init__(self, name):
        """Initialize StoreModel."""
        self.name = name

    def json(self):
        """Return json dictionary from StoreModel."""
        return {'name': self.name,
                'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        """Find Store by name."""
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        """Find Store by name."""
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        """Save StoreModel to DB."""
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """Delete Store from DB."""
        db.session.delete(self)
        db.session.commit()
