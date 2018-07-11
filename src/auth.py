"""Authentication wrapper."""
from flask import g
from flask_httpauth import HTTPBasicAuth
import sqlalchemy
import src.models as m

auth = HTTPBasicAuth()

@auth.get_password
def get_pw(username):
    try:
        user = m.User.query.filter(m.User.username == username).one_or_none()
    except sqlalchemy.exc.SQLAlchemyError:
        return None
    if user:
        g.nick = user.nick
        return user.password
    return None