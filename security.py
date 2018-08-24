"""Security definition."""
from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """Authenticate user by name and password."""
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """Get the identification from the user."""
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
