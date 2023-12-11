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


def drop_user():
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            drop = f'''DROP table if EXISTS Users'''
            cursor.execute(drop)
            db_connect.commit()
            print('[+] Users удалена')


def drop_cook():
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST) as db_connect:
        with db_connect.cursor() as cursor:
            drop = f'''DROP table if EXISTS CookForm'''
            cursor.execute(drop)
            db_connect.commit()
            print('[+] CookForm удалена')


drop_cook()
#drop_user()
#create_user_table()
create_cook_table()
