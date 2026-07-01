from add_expense import add_expense
from view_expense import view_expense
from update_expense import update_expense
from delete_expense import delete_expense
from total_expense import total_expense
from category_report import category_report
from search_expense import search_expense
from monthly_report import monthly_report
from highest_expense import highest_expense
from lowest_expense import lowest_expense

while True:
    print("\n=====Expense Tracker=====")
    print("""
        1.Add Expense
        2.View Expense
        3.Update Expense
        4.Delete Expense
        5.Total Expense
        6.Category Report
        7.Search Results
        8.Monthly Report
        9.Highest Expense
        10.Lowest Expense
        11.Exit
    """ )

    choice=input("Enter your choice: ")

    if choice=="1":
        print("Add expense selected")
        add_expense()
    elif choice=="2":
        print("View expenses selected")
        view_expense()
    elif choice=="3":
        print("Update expenses selected")
        update_expense()
    elif choice=="4":
        print("Delete expenses selected")
        delete_expense()
    elif choice=="5":
        total_expense()
    elif choice=="6":
        category_report()
    elif choice=="7":
        search_expense()
    elif choice=="8":
        monthly_report()
    elif choice=="9":
        highest_expense()
    elif choice=="10":
        lowest_expense()
    elif choice=="11":
        print("Thank you for selecting Expense Tracker")
        break
    else:
        print("Invalid choice")
