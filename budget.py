from db import connection, cursor
from datetime import datetime

def save_budget(amount):
    current_month = datetime.now().strftime("%Y-%m")
    query="""
    INSERT INTO budget(month,amount)
    VALUES(%s,%s)
    ON DUPLICATE KEY UPDATE
    amount=%s
    """
    values=(current_month,amount,amount)
    cursor.execute(query,values)
    connection.commit()
def get_budget():
    current_month = datetime.now().strftime("%Y-%m")
    query="""
    SELECT amount
    FROM budget
    WHERE month=%s
    """
    values=(current_month,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    if result:
        return float(result[0])
    return 0