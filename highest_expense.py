from db import connection, cursor

def highest_expense_terminal():
    query="""
    SELECT * 
    FROM expenses
    ORDER BY amount DESC
    LIMIT 1
    """
    cursor.execute(query)  
    expense=cursor.fetchone()

    if expense is None:
        print("No eexpenses found")
    else:
        print("\n====Highest expense====")
        print(f"ID          : {expense[0]}")
        print(f"Amount      : ₹{expense[1]}")
        print(f"Category    : {expense[2]}")
        print(f"Description : {expense[3]}")
        print(f"Date        : {expense[4]}")
def highest_expense():
    query="""
    SELECT * 
    FROM expenses
    ORDER BY amount DESC
    LIMIT 1
    """
    cursor.execute(query)  
    return cursor.fetchone()

