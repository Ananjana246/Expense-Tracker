from db import connection, cursor

def search_expense_terminal():

    category=input("Enter the category to search: ").lower()
    query="""
    SELECT *
    FROM expenses 
    WHERE category = %s
    """
    values=(category,)
    cursor.execute(query,values)
    expenses=cursor.fetchall()

    if len(expenses)==0:
        print("\nNo expenses found for this category.")
    else:
        print("\n=====Search Results=====")
        for expense in expenses:
           print(
                f"ID          : {expense[0]} \n "
                f"Amount      : ₹{expense[1]} \n "
                f"Category    : {expense[2]} \n "
                f"Description : {expense[3]} \n "
                f"Date        : {expense[4]}"
           )
def search_expense(category):
    query="""
    SELECT *
    FROM expenses 
    WHERE category = %s
    """
    values=(category,)
    cursor.execute(query,values)
    return cursor.fetchall()

