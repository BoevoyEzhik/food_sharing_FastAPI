from fastapi import APIRouter, Request
from app.services.v1.cook_form import process_update_cook

from app.api.models.cook_form import UpdateCookForm


update_cook = APIRouter()


@update_cook.put('/update-cook-form')
def update_cook_info(cook_form: UpdateCookForm, request: Request):
    token = request.cookies.get('user_id')
    if token:
        result = process_update_cook(cook_form, token)
        if result:
            return {'status': 200}
    return {'status': 401, 'text': 'unexpected error'}
