


import pandas as pd

# Data input
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Creating a Pandas Series
exam_scores = pd.Series(data=exam_scores, index=students, name="Exam Scores")

# Displaying the Series
print(exam_scores)


"""
OUTPUT

====== RESTART: C:/Users/Mayur Manwar/Desktop/lab_code/Pandas_Series 1.py ======
Alice      92
Bob        88
Charlie    76
David      94
Eve        82
Frank      90
Grace      85
Hannah     89
Ivy        78
Jack       91
Name: Exam Scores, dtype: int64

"""
