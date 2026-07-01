from db import connection, cursor
def view_expense_terminal():
    query="""
    SELECT * FROM expenses;
    """

    cursor.execute(query)
    expenses=cursor.fetchall()

    for expense in expenses:
        # print(expense)
        print(
            f"ID           : {expense[0]},\n "
            f"Amount      : ₹{expense[1]},\n "
            f"Category    : {expense[2]},\n "
            f"Description : {expense[3]},\n "
            f"Date        : {expense[4]}"
        )

def view_expense():
    query="SELECT * FROM expenses"
    cursor.execute(query)
    return cursor.fetchall()

