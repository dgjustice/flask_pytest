"""DB models for our application."""
from src import DB
# pylint: disable=no-member,too-few-public-methods

class User(DB.Model):
    """Model representing a user object."""
    username = DB.Column(DB.String, primary_key=True)
    password = DB.Column(DB.String, nullable=False)
    nick = DB.Column(DB.String, nullable=False)

class Message(DB.Model):
    """Message model."""
    message_id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    username = DB.Column(DB.String, DB.ForeignKey(
        f"{User.__tablename__}.username"
    ), nullable=False)
    message_text = DB.Column(DB.String, nullable=False)
