import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ananjana@123",   
    database="expense_tracker"
)

if connection.is_connected():
    print("Connected to MySQL successfully!")