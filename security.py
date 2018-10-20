from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id : u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password): # safer for different encoding cases, than string == string
        return user

def identity(payload):
    userid=payload['identity']
    return userid_mapping.get(userid, None)