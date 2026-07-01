  # Expense Tracker

A command-line Expense Tracker built with Python and MySQL.

## Features

-   Add expenses
-   View all expenses
-   Update expenses
-   Delete expenses
-   Total expense summary
-   Category-wise expense report
-   Search expenses by category
-   Highest expense finder
-   Input validation for amount, dates, and IDs

## Technologies Used

-   Python
-   MySQL
-   mysql-connector-python
-   python-dotenv
-   Git and GitHub

## Project Structure

``` text
Project_expense/
│
├── add_expense.py
├── view_expense.py
├── update_expense.py
├── delete_expense.py
├── total_expense.py
├── category_report.py
├── search_expense.py
├── highest_expense.py
├── db.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

1.  Clone the repository.
2.  Create and activate a virtual environment.
3.  Install dependencies:

``` bash
pip install -r requirements.txt
```

4.  Create a `.env` file with your database credentials.
5.  Run the application:

``` bash
python3 main.py
```

## Author

Ananjana K
