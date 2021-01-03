import pytest
from common.app import create_app

@pytest.fixture
def create_test_app():
    app = create_app()
    app.config.update['MONGODB_SETTINGS'] = {
            'db': 'blog_test',
            'host': "cluster0.qabhw.mongodb.net",
            'username': 'root',
            'password': 'root1234'
        }
    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:

        yield client
