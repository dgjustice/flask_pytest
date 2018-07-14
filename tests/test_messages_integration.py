"""Message app test runner."""
import os
import base64
from functools import wraps
from pathlib import Path
import pytest
import json
from unittest.mock import Mock, patch, MagicMock
from flask import g
from src.app import create_app
import src.models as m
from tests.load_db_data import init_db

@pytest.fixture
def app_inst():
    """Pytest fixture that returns an instance of our application."""
    app = create_app()
    app.debug = True
    # Load test DB objects
    init_db(app)
    return app

def test_get_messages_401(app_inst):
    """Send a GET with no auth header or bad auth and expext 401."""
    client = app_inst.test_client()
    rv = client.get("/app/messages")
    assert rv.status_code == 401
    auth_str = base64.b64encode(b"foo:bad_pass").decode("utf-8")
    rv = client.get("/app/messages", headers={"Authorization": f"Basic {auth_str}"})
    assert rv.status_code == 401

def test_get_message_200(app_inst):
    """Send a GET with good auth and expect a message."""
    client = app_inst.test_client()
    auth_str = base64.b64encode(b"foo:foo_pass").decode("utf-8")
    rv = client.get("/app/messages", headers={"Authorization": f"Basic {auth_str}"})
    assert rv.status_code == 200
    assert b'"user": "foo"' in rv.data
