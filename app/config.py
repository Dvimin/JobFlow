from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "dbname": os.getenv("DB_NAME", "hh_analytics"),
    "user": os.getenv("DB_USER", "hh_user"),
    "password": os.getenv("DB_PASSWORD", "hh_password"),
}