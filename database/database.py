import psycopg2
from psycopg2.extras import DictCursor
from time import sleep
import config as conf

# connection to databse
cursor=None
while not cursor:
    try:
        conn = psycopg2.connect(host=conf.DB_HOST, database=conf.DB_NAME, user=conf.DB_USER, password=conf.DB_PASS,
                                cursor_factory=DictCursor)
        cursor = conn.cursor()
        print("database successful connection")
        break
    except Exception as ex:
        print("Error: " + str(ex))
        sleep(2)