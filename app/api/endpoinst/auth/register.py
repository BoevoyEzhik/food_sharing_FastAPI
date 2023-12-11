from fastapi import APIRouter
from app.api.models.auth import User
from app.services.auth.auth import reg_user
import re
from datetime import date

register = APIRouter()


@register.post('/register')
def register_user(user: User):
    if not _is_valid_email(user.email):
        return {'status': 301, 'text': 'invalid email'}
    if not _is_valid_age(user.birthday):
        return {'status': 301, 'text': 'incorrect age'}
    reg_user(user)
    return {'status': 200, 'text': 'success'}


def _is_valid_email(email):
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    if re.fullmatch(regex, email):
        return True
    return False


def _is_valid_age(birthday):
    today = date.today()
    if today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)) + 1 > 120:
        return 'invalid age'
    else:
        return birthday
