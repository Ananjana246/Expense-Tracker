import mysql.connector
import os
from dotenv import load_detenv
load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor=connection.cursor()

amount=float(input("Enter the amount: "))
category=input("Enter category: ")
description=input("Enter the description: ")
expense_date=input("Enter the date: ")

query="""
INSERT INTO expenses(amount, category, description, expense_date)
VALUES(%s, %s, %s, %s)
"""
values=(amount,category,description,expense_date)

cursor.execute(query, values)
connection.commit()

print("Expense added successfully!")

cursor.close()
connection.close()