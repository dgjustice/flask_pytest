"""Initialization script to load test data into the DB."""
import src.models as m
from src import DB

def init_db(app):
    """Init the DB with some fake data."""
    with app.app_context():
        DB.create_all()
        db_items = [
            m.User(
                username="foo",
                password="foo_pass",
                nick="foober"
            ),
            m.User(
                username="bar",
                password="bar_pass",
                nick="barber"
            ),
            m.User(
                username="qud",
                password="qud_pass",
                nick="qudber"
            ),
            m.Message(
                username="foo",
                message_text="Goofy message from foo!"
            ),
            m.Message(
                username="foo",
                message_text="Another message from foo!"
            ),
            m.Message(
                username="bar",
                message_text="Bar says hello!"
            ),
            m.Message(
                username="qud",
                message_text="Qud wants to go to the movies!"
            ),
        ]
        for item in db_items:
            # pylint: disable=no-member
            DB.session.merge(item)
            DB.session.commit()