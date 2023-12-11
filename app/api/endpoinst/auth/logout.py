from fastapi import APIRouter, Response


logout = APIRouter()


@logout.post('/logout')
def logout_user(response: Response):
    response.delete_cookie('user_id')
    return {'status': 200, 'text': 'ok'}

