from flask import Flask
from src import DB
from src.pages_bp import bp as pages_bp
import src.models as m

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages_bp, url_prefix="/pages")
    DB.init_app(app)
    with app.app_context():
        DB.create_all()
        users = [
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
        ]
        for user in users:
            DB.session.merge(user)
            DB.session.commit()
    return app
