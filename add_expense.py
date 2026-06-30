import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ananjana@123",   
    database="expense_tracker"
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