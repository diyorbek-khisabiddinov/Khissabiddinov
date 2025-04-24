import psycopg2
from config import load_config

def upsert(name, phone):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('call upsert(%s, %s)', (name, phone))
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

name, phone = input("Enter a new name: "), input("Enter a new phone: ")
upsert(name, phone)