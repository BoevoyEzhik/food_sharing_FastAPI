from fastapi import APIRouter, Cookie
from app.services.v1.update_user import process_update_user


update_user = APIRouter()


@update_user.put('/update-user-info')
def update_user_info(info):
    token = Cookie()
    if token:
        process_update_user(info)
        return {'status': 200}
    return {'status': 401, 'text': 'unexpected error'}