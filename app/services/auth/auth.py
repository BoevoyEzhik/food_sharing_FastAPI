import uuid
import os
import hashlib
from datetime import datetime
from app.db.db_user import add_user, get_user_by_email


def reg_user(user):
    now = datetime.now()
    id_ = str(uuid.uuid4())
    user.password = _generating_hash(user.password)
    info = (id_, user.first_name, user.last_name, user.birthday, user.city, user.sex, user.email, user.password, now, now)
    print(info)
    add_user(info)


def start_login(login_info):
    user_info = get_user_by_email(login_info.email)
    if not user_info:
        return 'user not registered'
    elif not _check_password(login_info.password, user_info[7]):
        return 'wrong login or password'
    return user_info[0]


def _generating_hash(password):
    salt = os.urandom(16).hex()
    key = hashlib.sha512(password.encode() + salt.encode()).hexdigest()
    result = (key + salt)
    return result


def _check_password(password, password_hash):
    salt = password_hash[128:]
    key = hashlib.sha512(password.encode() + salt.encode()).hexdigest()
    result = (key + salt)
    if password_hash == result:
        return True
    return False
