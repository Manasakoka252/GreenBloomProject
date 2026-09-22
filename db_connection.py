import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="green_bloom_db"
    )

    return connection

connection = create_connection()

if connection.is_connected():
    print("MySQL connection successful!")
    connection.close()
