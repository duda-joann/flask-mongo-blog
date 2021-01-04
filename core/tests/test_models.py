import datetime

def test_new_user(user):
    assert user.email == 'test@test.py'
    assert user.username == 'Testik'
    #assert user.hashed_password == 'password1'
    #how to check if password is saved and compare with hash password,
    # but password is hashed during registration not during creation


def test_new_post(post):
    assert post.title == 'Test'
    assert post.body == 'TestTestTestumTestumem'
    assert post.published is True
    assert post.author == 'Testik'
    assert post.creation != datetime.datetime.now


def test_new_tag(tag):
    assert tag.name == 'test'
    assert tag.creation != datetime.datetime.now







