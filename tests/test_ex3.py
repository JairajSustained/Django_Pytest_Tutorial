# import pytest

# from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user("testuser", "test@example.com", "password")
#     count = User.objects.all().count()
#     print(count)
#     assert User.objects.count() == 1


# @pytest.mark.django_db
# def test_user_create_2():
#     count = User.objects.all().count()
#     print(count)
#     assert User.objects.count() == 0
