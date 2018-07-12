"""Main application module that wraps up blueprints and app factory."""
from flask import Flask
from src.message_bp import BP as message_bp
from src import DB

def create_app():
    """Flask app factory, returns app instance."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.register_blueprint(message_bp, url_prefix="/app")
    DB.init_app(app)
    return app
