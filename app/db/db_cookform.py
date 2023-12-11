import psycopg2
from app.db.db_config import DB_NAME, USER, PASSWORD, HOST


def create_cook_table():
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS CookForm
                                (id UUID PRIMARY KEY UNIQUE,
                                user_id UUID NOT NULL,
                                title varchar (120) NOT NULL,
                                description varchar (3000) NOT NULL,
                                active bool NOT NULL,
                                FOREIGN KEY (user_id) REFERENCES Users (id)
                                )''')
            db_connect.commit()
            print('[+] CookForm создана')


class CookForm:
    def __int__(self, db_name, user, password, host):
        self.connection = psycopg2.connect(
            db_name=db_name,
            user=user,
            password=password,
            host=host
        )

    def create_cook(self, info_to_insert: tuple):
        insert_query = f'''INSERT INTO CookForm (
                        id, user_id, title, active
                        )
                        VALUES (%s, %s, %s, %s)'''
        with self.connection.cursor() as cursor:
            cursor.execute(insert_query, info_to_insert)
            self.connection.commit()

    def update_cook(self, info: dict[str: str | bool]):
        cook_id = info.pop('id')
        with self.connection.cursor() as cursor:
            for key, value in info.items():
                update_query = f'''UPDATE CookForm set {key} = %s where id=%s'''
                cursor.execute(update_query, (value, cook_id))
                self.connection.commit()

    def get_all_cook(self, limit, offset):
        select_by_count = f'''SELECT * FROM CookForm
                            LIMIT {limit} 
                            OFFSET {offset}'''
        with self.connection.cursor() as cursor:
            cursor.execute(select_by_count)
            result = cursor.fetchall()
            return result

    def get_my_all_cook(self, user_id, limit, offset):
        select_by_count = f'''SELECT * FROM CookForm 
                            WHERE user_id = {user_id} 
                            LIMIT {limit} 
                            OFFSET {offset}'''
        with self.connection.cursor() as cursor:
            cursor.execute(select_by_count)
            result = cursor.fatchall()
            return result


# ------------------------------------------------------------------------------------------------- #
def create_cook(info_to_insert: tuple):
    insert_query = f'''INSERT INTO CookForm (
                            id, user_id, title, description, active
                            )
                            VALUES (%s, %s, %s, %s, %s)'''
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute(insert_query, info_to_insert)
            db_connect.commit()


def update_cook(info):
    cook_id = info.pop('id')
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            for key, value in info.items():
                if value:
                    update_query = f'''UPDATE CookForm set {key}=%s where id=%s'''
                    cursor.execute(update_query, (value, cook_id))
                    db_connect.commit()


def get_all_cook(limit, offset):
    select_by_count = f'''SELECT * FROM CookForm
                        LIMIT {limit} 
                        OFFSET {offset}'''
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute(select_by_count)
            result = cursor.fetchall()
            return result


def get_my_all_cook(user_id, limit, offset):
    select_by_count = f'''SELECT * FROM CookForm 
                        WHERE user_id = %s 
                        LIMIT {limit} 
                        OFFSET {offset}'''
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute(select_by_count, (user_id, ))
            result = cursor.fetchall()
            return result


def select_all():
    select_by_count = f'''SELECT * FROM CookForm'''
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute(select_by_count)
            result = cursor.fetchall()
            return result

