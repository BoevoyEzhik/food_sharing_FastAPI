from fastapi import APIRouter, Cookie, Request
from app.services.v1.cook_form import process_create_cook

from app.api.models.cook_form import CreateCookForm


create_cook = APIRouter()


@create_cook.post('/create-cook-form')
def create_cook_info(cook_form: CreateCookForm, request: Request):
    token = request.cookies.get('user_id')
    if token:
        process_create_cook(cook_form, token)
        return {'status': 200}
    return {'status': 401, 'text': 'unexpected error'}