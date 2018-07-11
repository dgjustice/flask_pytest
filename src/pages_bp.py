from flask import Blueprint
from src.auth import auth

bp = Blueprint("pages", __name__)

@bp.route("/")
@auth.login_required
def show_page():
    return "Hello world!"
