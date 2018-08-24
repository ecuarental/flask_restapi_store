"""User model definition."""
from db import db


class UserModel(db.Model):
    """UserModel class definition."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        """Initialize UserModel."""
        self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        """Save user to DB."""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        """Find user by name."""
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        """Find user by id."""
        return cls.query.filter_by(id=_id).first()
