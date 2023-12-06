from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME_RAW = os.environ.get("DB_NAME_RAW")
DB_NAME_ORM = os.environ.get("DB_NAME_ORM")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
SECRET_AUTH = os.environ.get("SECRET_AUTH")
SECRET_MANAGER= os.environ.get("SECRET_MANAGER")
