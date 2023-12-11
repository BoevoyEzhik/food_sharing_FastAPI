from app.db.db_cookform import create_cook, update_cook, get_all_cook, get_my_all_cook
from app.db.db_user import get_user_by_id
import uuid
from app.services.auth.cookie_jwt import get_id_from_jwt


def process_create_cook(cook_form, token):
    cook_id = str(uuid.uuid4())
    user_id = get_id_from_jwt(token)
    create_cook((cook_id, user_id, cook_form.title, cook_form.description, cook_form.active))
    return True


def process_update_cook(cook_form, token):
    try:
        user_id = get_id_from_jwt(token)
        pass
    except:
        return False
    user_in_db = get_user_by_id(user_id)
    if user_in_db:
        info = {'id': str(cook_form.id),
                'title': cook_form.title,
                'description': cook_form.description,
                'active': cook_form.active}
        update_cook(info)
    return True


def process_get_my_all_cook_form(token, limit, offset):
    user_id = get_id_from_jwt(token)
    result = get_my_all_cook(str(user_id), limit, offset)
    return result


def process_get_all_cook_form(limit, offset):
    result = get_all_cook(limit, offset)
    return result
