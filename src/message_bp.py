"""Messages view module"""
import json
import sqlalchemy
from flask import Blueprint, g, abort, Response
from src.auth import AUTH
import src.models as m

BP = Blueprint("app", __name__)

def get_messages():
    """Retrieve messages from the DB by user."""
    try:
        messages = m.Message.query.filter(
            m.Message.username == g.user.username
        ).all()
    except sqlalchemy.exc.SQLAlchemyError:
        abort(500, "Could not retrieve records from the DB.")
    # print(messages)
    resp_text = json.dumps([
        {
            "user": message.username,
            "message_text": message.message_text
        }
        for message in messages
    ])
    return resp_text

@BP.route("/messages")
@AUTH.login_required
def show_messages():
    """Show messages by user."""
    resp_text = get_messages()
    return Response(resp_text, mimetype="application/json")
