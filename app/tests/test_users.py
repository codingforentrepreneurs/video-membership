import pytest
from app import db
from app.users.models import User

@pytest.fixture(scope='module')
def setup():
    # setup
    session = db.get_session()
    yield session
    # teardown
    q = User.objects.filter(email='test@test.com')
    if q.count() != 0:
        q.delete()
    session.shutdown()

def test_create_user(setup):
    User.create_user(email='test@test.com', password='abc123')

def test_duplicate_user(setup):
    with pytest.raises(Exception):
        User.create_user(email='test@test.com', password='abc123dafd')

def test_invalid_email(setup):
    with pytest.raises(Exception):
        User.create_user(email='test@test', password='abc123dafd')

def test_valid_password(setup):
    q = User.objects.filter(email='test@test.com')
    assert q.count() == 1
    user_obj = q.first()
    assert user_obj.verify_password('abc123') == True
    assert user_obj.verify_password('abc1234') == False

# def test_assert():
#     assert True is True


# def test_equal():
#     assert 1 == 1

# def test_equal():
#     assert 1 != 1

# def test_invalid_assert():
#     with pytest.raises(AssertionError):
#         assert True is not True