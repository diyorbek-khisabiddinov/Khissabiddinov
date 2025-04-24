import psycopg2
from config import load_config

def get_record(pattern):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("select get_records(%s)", (pattern,))
                result = cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return result

pattern = input("Enter a pattern: ")
res = get_record(pattern)
print(*res)