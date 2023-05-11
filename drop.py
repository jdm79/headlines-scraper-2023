import database
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

MY_DB_URL = os.getenv('MY_DB_URL')

connection = psycopg2.connect(MY_DB_URL)

database.create_tables(connection)
database.drop_tables(connection)