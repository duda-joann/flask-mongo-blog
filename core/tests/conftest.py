import pytest
from common.app import create_app
from models.users import Users
from models.posts import Posts
from models.tags import Tags


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


@pytest.fixture
def create_user():
    user = Users(username='Testik', email='test@test.py', password='password1')
    user.save()

    yield user


@pytest.fixture
def create_tag():
    tag = Tags(name='test')
    tag.save()
    yield tag


@pytest.fixture
def create_post():
    post = Posts(tittle = 'Test', body='TestTestTestumTestumem', published = True, author= 'Testik')
    post.save()
    yield post



