from fastapi import APIRouter, Request
from app.services.v1.cook_form import process_get_my_all_cook_form


get_my_all_cook_form = APIRouter()


@get_my_all_cook_form.get('/get-my-all-cook-form/{cook_id}')
def get_my_all_cook_form_info(limit: int, offset: int, request: Request):
    token = request.cookies.get('user_id')
    if token:
        result = process_get_my_all_cook_form(token, limit, offset)
        return result
    return {'status': 401, 'text': 'unexpected error'}
