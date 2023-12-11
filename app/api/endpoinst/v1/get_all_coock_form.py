from fastapi import APIRouter
from app.services.v1.cook_form import process_get_all_cook_form


get_all_cook_form = APIRouter()


@get_all_cook_form.get('/get-all-cook-form/')
def get_all_cook_form_info(limit: int, offset: int):
    result = process_get_all_cook_form(limit, offset)
    if result:
        return result
    return {'status': 401, 'text': 'unexpected error'}
