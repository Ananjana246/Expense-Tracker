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