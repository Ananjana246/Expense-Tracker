import mysql.connector
import os
from dotenv import load_detenv
load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
    # host="localhost",
    # user="root",
    # password="Ananjana@123",   
    # database="expense_tracker"
)

if connection.is_connected():
    print("Connected to MySQL successfully!")