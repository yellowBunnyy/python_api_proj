from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    """Create model to db.

    Args:
        UserMixin (_type_): _description_
        db (_type_): _description_
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
