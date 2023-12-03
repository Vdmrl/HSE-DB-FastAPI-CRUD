import psycopg2
from psycopg2.extras import DictCursor
from time import sleep

# connection to databse
cursor=None
while not cursor:
    try:
        print("password: ", end="")
        conn = psycopg2.connect(host="localhost", database="hse_db_course", user="postgres", password=input(),
                                cursor_factory=DictCursor)
        cursor = conn.cursor()
        print("database successful connection")
        break
    except Exception as ex:
        print("Error: " + str(ex))
        sleep(2)