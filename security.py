from werkzeug.security import safe_str_cmp
from user import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):  # safer for different encoding cases, than string == string
        return user


def identity(payload):
    userid = payload['identity']
    return User.find_by_id(userid)
