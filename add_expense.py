from db import connection, cursor
from datetime import datetime

def add_expense_terminal():
    while True:
        try:
            amount=float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        category=input("Enter category: ").strip().lower()
        if category:
            break
        print("Category cannot be empty")
    while True:
        description=input("Enter description: ").strip()
        if description:
            break
        print("Description cannot be empty")
    while True:
        expense_date=input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(expense_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    query="""
    INSERT INTO expenses(amount, category, description, expense_date)
    VALUES(%s, %s, %s, %s)
    """
    values=(amount,category,description,expense_date)

    cursor.execute(query, values)
    connection.commit()

    print("Expense added successfully!")

def add_expense(amount,category,description,expense_date):
    query="""
    INSERT INTO expenses(amount, category, description, expense_date)
    VALUES(%s, %s, %s, %s)
    """
    values=(amount,category,description,expense_date)

    cursor.execute(query, values)
    connection.commit()
    