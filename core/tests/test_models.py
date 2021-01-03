from models.users import Users


def test_new_user():
    user = Users(username='Testik', email = 'test@test.py', password='password1')
    user.save()
    assert user.email == 'test@test.py'
    assert user.username == 'Testik'
    #assert user.hashed_password == 'password1'
    #how to check if password is saved and compare with hash password,
    # but password is hashed during registration not during creation


def test_new_post():
    pass






