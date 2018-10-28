from werkzeug.security import safe_str_cmp
from models.usermodel import UserModel
from db import db

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    # print(username)
    # print(password)
    # print(user)
    if user and safe_str_cmp(user.password, password):  # safer for different encoding cases, than string == string
        return user


def identity(payload):
    userid = payload['identity']
    return UserModel.find_by_id(userid)
