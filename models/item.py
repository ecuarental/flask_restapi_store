"""Item Model definition."""
from db import db


class ItemModel(db.Model):
    """Item model class definition."""

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel', back_populates="items")

    def __init__(self, name, price, store_id):
        """Init Item model object."""
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        """Return json dictionary of the item."""
        return {'name': self.name,
                'price': self.price,
                'store_name': self.store.name,
                'store_id': self.store.id}

    @classmethod
    def find_by_name(cls, name):
        """Find item by name."""
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        """Insert item."""
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """Delete from db."""
        db.session.delete(self)
        db.session.commit()
