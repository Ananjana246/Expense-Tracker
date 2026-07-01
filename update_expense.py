from db import connection, cursor

def update_expense_terminal():
    expense_id=int(input("Enter Expense ID to update: "))
    cursor.execute(
        "SELECT * FROM expenses WHERE id=%s",
        (expense_id,)  
    )
    if cursor.fetchone() is None:
        print("Expense ID not found.")
        return

    new_amount=float(input("Enter the amount: "))

    query="""
    UPDATE expenses
    SET AMOUNT=%s
    WHERE ID=%s
    """

    values=(new_amount,expense_id)

    cursor.execute(query,values)
    connection.commit()
    print("Expenses updated successfully!")
def update_expense(expense_id,new_amount):

    query="""
    UPDATE expenses
    SET AMOUNT=%s
    WHERE ID=%s
    """

    values=(new_amount,expense_id)
    
    cursor.execute(query,values)
    connection.commit()
    return cursor.rowcount


