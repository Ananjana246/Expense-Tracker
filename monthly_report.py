from db import connection, cursor

def monthly_report_terminal():
    month=input("Enter the month(YYYY:MM): ")
    query="""
    SELECT SUM(amount)
    FROM expenses
    WHERE MONTH(expense_date)=%s
    AND YEAR(expense_date)=YEAR(CURDATE())
    """
    values=(month,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    total=result[0]

    if total is None:
        total=0
    print(f"\nTotal expenses for {month}:₹{total}")
def monthly_report(month_number):
    query="""
    SELECT SUM(amount)
    FROM expenses
    WHERE MONTH(expense_date)=%s
    AND YEAR(expense_date)=YEAR(CURDATE())
    """
    values=(month_number,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    total=result[0]

    if total is None:
        total=0
    return total


