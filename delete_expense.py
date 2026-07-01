from db import connection, cursor

def delete_expense_terminal():
    expense_id=int(input("Enter the expense ID to delete: "))
    cursor.execute(
        "SELECT * FROM expenses WHERE id=%s",
        (expense_id,)
    )
    if cursor.fetchone() is None:
        print("Expense ID not found.")
        return
    confirm=input("Are you sure you want to delete this expense?(y/n): ").lower()
    if confirm!="y":
        print("Deletion cancelled.")
        return

    query="""
    DELETE FROM expenses
    WHERE ID=%s
    """

    values=(expense_id,)
    cursor.execute(query,values)
    connection.commit()

    if cursor.rowcount>0:
        print("Expense delete successfully")
    else:
        print("Expense ID not found")
def delete_expense(expense_id):

    query="""
    DELETE FROM expenses
    WHERE ID=%s
    """

    values=(expense_id,)
    cursor.execute(query,values)
    connection.commit()

    return cursor.rowcount



