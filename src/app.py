"""Main application module that wraps up blueprints and app factory."""
from flask import Flask
from src import DB
from src.message_bp import BP as message_bp
import src.models as m

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

def create_app():
    """Flask app factory, returns app instance."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.register_blueprint(message_bp, url_prefix="/app")
    DB.init_app(app)
    # Create some dummy objects for demo purposes
    init_db(app)
    return app
