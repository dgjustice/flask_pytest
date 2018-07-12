"""Authentication wrapper."""
from flask import g
from flask_httpauth import HTTPBasicAuth
import sqlalchemy
import src.models as m

AUTH = HTTPBasicAuth()

@AUTH.get_password
def get_pw(username):
    """Retrieve user object from the DB and check the password."""
    try:
        user = m.User.query.filter(m.User.username == username).one_or_none()
    except sqlalchemy.exc.SQLAlchemyError:
        return None
    if user:
        g.user = user
        return user.password
    return None
