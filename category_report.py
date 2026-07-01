from db import connection, cursor

def category_report_terminal():
    query="""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """
    cursor.execute(query)
    results=cursor.fetchall()
    print("\n=====Expenses by category====")
     
    for row in results:
        category=row[0]
        total=row[1]

        print(f"{category}:₹{total}")
def category_report():
    query="""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """
    cursor.execute(query)
    return cursor.fetchall()


