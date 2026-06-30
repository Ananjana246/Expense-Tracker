import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ananjana@123",   
    database="expense_tracker"
)

cursor=connection.cursor()

query="""
SELECT * FROM expenses;
"""

cursor.execute(query)
expenses=cursor.fetchall()

for expense in expenses:
    # print(expense)
    print(
        f"ID: {expense[0]}, "
        f"Amount: ₹{expense[1]}, "
        f"Category: {expense[2]}, "
        f"Description: {expense[3]}, "
        f"Date: {expense[4]}"
    )

cursor.close()
connection.close()