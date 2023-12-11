from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    first_name: str
    last_name: str
    birthday: date
    city: str
    sex: str
    email: str
    password: str


class Login(BaseModel):
    email: str
    password: str

# my_dict = {'firstname': 'Nikita',
#            'lastname': 'Z',
#            'birthday': '1900-12-05',
#            'city': 'Moscow',
#            'sex': 123,
#            'email': 'nikita120597@mail.ru',
#            'password': 'qwerty'}
#
# user = User(**my_dict)
#
# print(user)
# user.password = generating_hash(user.password)
#
# print(user)