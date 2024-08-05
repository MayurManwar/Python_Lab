

import pandas as pd

# Expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Monthly expense data (example data in USD)
expenses = [500, 200, 1200, 300, 150]

# Creating a Pandas Series for expenses
expenses_series = pd.Series(data=expenses, index=categories, name="Monthly Expenses")

# Displaying the Series
print(expenses_series)


"""

Output

====== RESTART: C:/Users/Mayur Manwar/Desktop/lab_code/Pandas_Series 2.py ======
Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
Name: Monthly Expenses, dtype: int64

"""
