import pytest
from django.contrib.auth.models import User

# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user("test-user", "test@example.com", "password")
#     return user


# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-passwords") is True


# def test_check_username1(user_1):
#     print("test-1")
#     assert user_1.username == "test-user"


# def test_check_username2(user_1):
#     print("test-2")
#     assert user_1.username == "test-user"


# def test_new_user(new_user2):
#     print(new_user2.is_staff)
#     assert new_user2.is_staff


# @pytest.mark.django_db
# def test_new_user(new_user1):
#     print(new_user1.username)
#     assert True


def test_product(db, product_factory):
    product = product_factory.create()
    print(product.description)
    assert True
