from improved_test_code.repository import BaseRepo
from user.models import User
from user.serializer import UserSerilizer

user_repo = BaseRepo(User, UserSerilizer)
