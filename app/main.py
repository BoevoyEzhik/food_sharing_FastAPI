from fastapi import FastAPI
import uvicorn

from app.api.endpoinst.auth.register import register
from app.api.endpoinst.auth.login import login
from app.api.endpoinst.auth.logout import logout

from api.endpoinst.v1.create_cook_form import create_cook
from api.endpoinst.v1.update_cook_form import update_cook
from api.endpoinst.v1.get_my_all_cook_form import get_my_all_cook_form
from api.endpoinst.v1.get_all_coock_form import get_all_cook_form

from api.endpoinst.v1.update_user import update_user


app = FastAPI()

# auth
app.include_router(register, prefix='/auth')
app.include_router(login, prefix='/auth')
app.include_router(logout, prefix='/auth')

# v1
app.include_router(create_cook, prefix='/api/v1')
app.include_router(update_cook, prefix='/api/v1')
app.include_router(get_my_all_cook_form, prefix='/api/v1')
app.include_router(get_all_cook_form, prefix='/api/v1')
app.include_router(update_user, prefix='/api/v1')


if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=8000
                )
