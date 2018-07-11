"""DB models for our application."""
from src import DB

class User(DB.Model):
    username = DB.Column(DB.String, primary_key=True)
    password = DB.Column(DB.String, nullable=False)
    nick = DB.Column(DB.String, nullable=False)
