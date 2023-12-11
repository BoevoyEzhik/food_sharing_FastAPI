from fastapi import APIRouter, Response
from app.services.auth.auth import start_login
from app.api.models.auth import Login
from app.services.auth.cookie_jwt import create_jwt

login = APIRouter()


@login.post('/login')
def login_user(login_info: Login):
    result = start_login(login_info)
    if result == 'user not registered':
        return {'status': 401, 'text': 'user not registered'}
    elif result == 'wrong login or password':
        return {'status': 401, 'text': 'wrong login or password'}
    response = Response(status_code=200)
    response.set_cookie('user_id', create_jwt(result))
    return response
