from db import connection, cursor

def lowest_expense():
    query="""
    SELECT * 
    FROM expenses
    ORDER BY amount ASC
    LIMIT 1
    """
    cursor.execute(query)  
    expense=cursor.fetchone()

    if expense is None:
        print("No expenses found")
    else:
        print("\n====Lowest expense====")
        print(f"ID          : {expense[0]}")
        print(f"Amount      : ₹{expense[1]}")
        print(f"Category    : {expense[2]}")
        print(f"Description : {expense[3]}")
        print(f"Date        : {expense[4]}")
