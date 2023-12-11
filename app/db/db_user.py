import psycopg2
from app.db.db_config import DB_NAME, USER, PASSWORD, HOST


def create_user_table():
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
                                            id UUID PRIMARY KEY UNIQUE,
                                            first_name varchar NOT NULL,
                                            last_name varchar NOT NULL,
                                            birthday varchar NOT NULL,
                                            city varchar NOT NULL,
                                            sex varchar NOT NULL,
                                            email varchar UNIQUE NOT NULL,
                                            password_hash varchar NOT NULL,
                                            cdate timestamp,
                                            udate timestamp)''')
            db_connect.commit()
            print('[+] Users создана')


class User:
    def __int__(self):
        self.connection = psycopg2.connect(
            db_name=DB_NAME,
            user=USER,
            password=PASSWORD,
            host=HOST
        )

    def add_user(self, info_to_insert):
        insert_query = f'''INSERT INTO Users (
                        id, first_name, last_name, birthday, city, sex, email, password_hash, cdate, udate
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        with self.connection.cursor() as cursor:
            cursor.execute(insert_query, info_to_insert)
            self.connection.commit()

    def get_user_by_id(self, user_id):
        select_user = f"""SELECT * from Users where id = {user_id}"""
        with self.connection.cursor() as cursor:
            cursor.execute(select_user)
            result = cursor.fetchone()
            return result

    def get_user_by_email(self, email):
        select_user = f"""SELECT * from Users where email = {email}"""
        with self.connection.cursor() as cursor:
            cursor.execute(select_user)
            result = cursor.fetchone()
            return result

    def update_user(self, info):
        user_id = info.pop('user_id')
        with self.connection.cursor() as cursor:
            for key, value in info.items():
                update_query = f'''UPDATE Users set {key} = %s where user_id=%s'''
                cursor.execute(update_query, (value, user_id))
                self.connection.commit()

    def __del__(self):
        self.connection.close()


# ------------------------------------------------------------------------------------------------- #
def add_user(info_to_insert):
    insert_query = f'''INSERT INTO Users (
                            id, first_name, last_name, birthday, city, sex, email, password_hash, cdate, udate
                            )
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute(insert_query, info_to_insert)
            db_connect.commit()


def get_user_by_id(user_id):
    select_user = f"""SELECT * from Users where id = %s"""
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute(select_user, (user_id, ))
            result = cursor.fetchone()
            return result


def get_user_by_email(email):
    select_user = """SELECT * FROM Users WHERE email= (%s)"""
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute(select_user, [email])
            result = cursor.fetchone()
            return result


def update_user(info):
    user_id = info.pop('user_id')
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            for key, value in info.items():
                update_query = f'''UPDATE Users set {key} = %s where user_id=%s'''
                cursor.execute(update_query, (value, user_id))
                db_connect.commit()


def select_all_users():
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute('''SELECT * FROM Users''')
            result = cursor.fetchall()
            return result
