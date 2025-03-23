import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user_1(db):
    user = User.objects.create_user("test-user", "test@example.com", "password")
    print("create-user")
    return user


@pytest.fixture()
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@example.com",
        is_staff: bool = False,
        is_superuser: bool = False,
        is_active: bool = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user

    return create_app_user


@pytest.fixture
def new_user1(db, new_user_factory):
    return new_user_factory(
        username="user-A",
        password="password",
        first_name="A_name",
    )


@pytest.fixture
def new_user2(db, new_user_factory):
    return new_user_factory(
        username="user-A",
        password="password",
        first_name="A_name",
        is_staff=True,
    )
