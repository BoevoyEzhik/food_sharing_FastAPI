import jwt


SECRET = 'my-secret'


def create_jwt(user_id):
    payload = {'user_id': user_id}
    token = jwt.encode(payload, SECRET, algorithm='HS256')
    return token


def get_id_from_jwt(token):
    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
    return decoded['user_id']

