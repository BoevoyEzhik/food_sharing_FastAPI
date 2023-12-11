from app.db.db_user import User


def process_update_user(info):
    user = User()
    user.update_user(info)
    del user
    return True
