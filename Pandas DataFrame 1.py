
# Write a Pandas program to create a dataframe from a dictionary and display it.

import pandas as pd

# Sample data
score = {
    'Math': [78, 85, 96, 80, 86],
    'English': [84, 94, 89, 83, 86],
    'Hindi': [86, 97, 96, 72, 83]
}

# Create DataFrame
df = pd.DataFrame(score)

# Display the DataFrame
print(df)


"""
OUTPOU

===== RESTART: C:/Users/Mayur Manwar/Desktop/lab_code/Pandas DataFrame 1.py ====
   Math  English  Hindi
0    78       84     86
1    85       94     97
2    96       89     96
3    80       83     72
4    86       86     83

"""
