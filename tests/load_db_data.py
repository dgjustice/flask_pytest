"""Initialization script to load test data into the DB."""
import random
import src.models as m
from src import DB
from faker import Faker

FAKER = Faker()

def init_db(app):
    """Init the DB with some fake data."""
    with app.app_context():
        DB.create_all()
        users = [
            m.User(
                username=FAKER.word(),
                password=FAKER.password(),
                nick="".join(FAKER.words())
            ) for number in range(10)
        ]
        # We need at least one we can predict
        users.append(m.User(username="foo", password="foo_pass", nick="foobar"))
        db_items = [
            *users,
            *[
                m.Message(
                    username=random.choice(users).username,
                    message_text=FAKER.catch_phrase()
                ) for number in range(10000)
            ]
        ]
        for item in db_items:
            # pylint: disable=no-member
            DB.session.merge(item)
            DB.session.commit()