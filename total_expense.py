from db import connection, cursor
 
def total_expense_terminal():
    query="""
    SELECT SUM(amount)
    FROM expenses
    """
    cursor.execute(query)
    result=cursor.fetchone()
    total=result[0]

    if total is None:
        total=0
    print(f"\nTotal Expense is ₹{total}")
def total_expense():

    query="""
    SELECT SUM(amount)
    FROM expenses
    WHERE MONTH(expense_date)=MONTH(CURDATE())
    AND YEAR(expense_date)=YEAR(CURDATE())
    """
    
    cursor.execute(query)
    result=cursor.fetchone()
    total=result[0]

    if total is None:
        total=0
    return total


