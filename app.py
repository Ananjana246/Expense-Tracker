import streamlit as st
from add_expense import add_expense
from view_expense import view_expense
from update_expense import update_expense
from delete_expense import delete_expense
from total_expense import total_expense
from category_report import category_report
from search_expense import search_expense
from highest_expense import highest_expense
from lowest_expense import lowest_expense
from monthly_report import monthly_report
from budget import save_budget,get_budget
import pandas as pd


st.title("Expense Tracker")
st.write("Welcome to Expense Tracker")
# page=st.sidebar.selectbox(
#     "MENU",
#     [
#         "Add Expenses",
#         "View Expenses",
#         "Update Expenses",
#         "Delete Expenses",
#         "Total Expenses",
#         "Category Report",
#         "Search Expense",
#         "Highest Expense",
#         "Lowest Expense",
#         "Monthly Report",
#         "Budget Tracker"
#     ]
# )
if "page" not in st.session_state:
    st.session_state.page = "Home"
if st.sidebar.button("Add Expense"):
    st.session_state.page = "Add Expenses"
if st.sidebar.button("View Expenses"):
    st.session_state.page = "View Expenses"
if st.sidebar.button("Update Expenses"):
    st.session_state.page = "Update Expenses"
if st.sidebar.button("Delete Expenses"):
    st.session_state.page = "Delete Expenses"
if st.sidebar.button("Total Expenses"):
    st.session_state.page = "Total Expenses"
if st.sidebar.button("Category Report"):
    st.session_state.page = "Category Report"
if st.sidebar.button("Search Expense"):
    st.session_state.page = "Search Expense"
if st.sidebar.button("Highest Expense"):
    st.session_state.page = "Highest Expense"
if st.sidebar.button("Lowest Expense"):
    st.session_state.page = "Lowest Expense"
if st.sidebar.button("Monthly Report"):
    st.session_state.page = "Monthly Report"
if st.sidebar.button("Budget Tracker"):
    st.session_state.page = "Budget Tracker"
page = st.session_state.page
if page=="Add Expenses":
    amount=st.number_input(
        "Amount",
        min_value=0.0,
        step=1.0)
    category=st.text_input("Category")
    description=st.text_input("Description")
    expense_date=st.date_input("Expense Date")
    if st.button("Add Expense"):
        add_expense(amount,category,description,expense_date)
        st.success("Expense added successfully!")
elif page=="View Expenses":
    expenses=view_expense()
    df=pd.DataFrame(
        expenses,
        columns=[
            "ID",
            "Amount",
            "Category",
            "Description",
            "Expense Date"
        ]
    )
    st.dataframe(df,hide_index=True)
elif page=="Update Expenses":
    st.header("Update expenses")
    expense_id=st.number_input(
        "Expense ID",
        min_value=1,
        step=1
    )
    new_amount=st.number_input(
        "New Amount",
        min_value=0.0,
        step=1.0
    )
    if st.button("Update Expense"):
        updated=update_expense(expense_id,new_amount)
        if updated:
            st.success("Expense updated successfully")
        else:
            st.error("Expense ID not found")
elif page=="Delete Expenses":
    st.header("Delete Expenses")
    expense_id=st.number_input(
        "Expense ID",
        min_value=1,
        step=1
    )
    if st.button("Delete Expenses"):
        deleted=delete_expense(expense_id)
        if deleted:
            st.success("Expense deleted successfully")
        else:
            st.error("Expense ID not found.")
elif page=="Total Expenses":
    total=total_expense()
    st.header("Total Expense")
    st.metric(
        label="Total Spent",
        value=f"₹{total}"
        )
elif page=="Category Report":
    st.header("Expense By Category")
    data=category_report()
    df=pd.DataFrame(
        data,
        columns=["Category","Total Amount"]
    )
    st.dataframe(df)
elif page=="Search Expense":
    st.header("Search Expense")
    category=st.text_input(
        "Enter Category"
    )
    if st.button("Search"):
        expenses=search_expense(category)
        if expenses:
            df=pd.DataFrame(
                expenses,
                columns=["ID",
                        "Amount",
                        "Category",
                        "Description",
                        "Expense-Date"
                        ]
            )
            st.dataframe(df)
        else:
            st.warning(
                "No expenses found."
            )
elif page=="Highest Expense":
    st.header("Highest Expense")
    expenses=highest_expense()
    if expenses:
        st.metric(
            "Highest Expense",
            f"₹{expenses[1]}"
        )
        st.write(f"Category:{expenses[2]}")
        st.write(f"Description:{expenses[3]}")
        st.write(f"Expense-Date:{expenses[4]}")
    else:
        st.warning("No expenses found.")
elif page=="Lowest Expense":
    st.header("Lowest Expense")
    expenses=lowest_expense()
    if expenses:
        st.metric(
            "Lowest Expense",
            f"₹{expenses[1]}"
        )
        st.write(f"Category:{expenses[2]}")
        st.write(f"Description:{expenses[3]}")
        st.write(f"Expense-Date:{expenses[4]}")
    else:
        st.warning("No expenses found.")
elif page=="Monthly Report":
    st.header("Monthly Report")
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    selected_month = st.selectbox(
        "Select Month",
        months
    )
    month_number = months.index(selected_month) + 1
    total=monthly_report(month_number)
    st.metric(
        f"{selected_month} Expenses",
        f"₹{total}"
        )
elif page=="Budget Tracker":
    st.header("Budget Tracker")
    current_budget=get_budget()
    budget=st.number_input(
        "Monthly Budget",
        min_value=0.0,
        value=0.0
    )
    if st.button("Save Budget"):
        save_budget(budget)
        st.success("Budget saves successfully")
        spent=total_expense()
        if spent is None:
            spent = 0
        remaining=current_budget-float(spent)

        col1,col2,col3=st.columns(3)
        with col1:
            st.metric("Budget",f"{current_budget}")
        with col2:
            st.metric("Spent",f"{spent}")
        with col3:
            st.metric("Remaining",f"{remaining}")
        if remaining<0:
            st.error(f"Budget exceeded by {abs(remaining)}")

 











