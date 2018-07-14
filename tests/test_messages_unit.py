"""Message app test runner."""
import os
import base64
from functools import wraps
from pathlib import Path
import pytest
import json
from unittest.mock import Mock, patch, MagicMock
from flask import g
from faker import Faker
from src.app import create_app
from src.message_bp import retrieve_message_text
import src.models as m
from tests.load_db_data import init_db

FAKER = Faker()

@pytest.fixture
def app_inst():
    """Pytest fixture that returns an instance of our application."""
    app = create_app()
    app.debug = True
    return app

@patch("src.message_bp.query_message_by_user")
def test_retrieve_message_text(mock_q, app_inst):
    """Send a GET with good auth and expect a message."""
    mock_q.return_value = [
        m.Message(username=FAKER.word(), message_text=FAKER.text())
            for number in range(10000)
    ]
    with app_inst.test_request_context("/app/messages"):
        # You *must* use an application or request context when dealing with Flask.g !!!
        g.user = MagicMock(username="not a user")
        resp = retrieve_message_text()
    assert json.loads(resp)