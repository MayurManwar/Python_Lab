import pandas as pd
import matplotlib.pyplot as plt

# Define the DataFrame
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group by 'school_code' and calculate mean, min, and max for 'age'
age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Display the results
print("Mean, Min, and Max age for each school:")
print(age_stats)

# Plot the results as horizontal bar charts
age_stats.plot(kind='barh', subplots=True, layout=(1, 3), figsize=(12, 6), color=['skyblue', 'lightgreen', 'salmon'])

# Add labels and title
plt.suptitle('Age Statistics by School Code')
plt.show()



"""
0utput

Mean, Min, and Max age for each school:
             mean  min  max
school_code                
s001         12.5   12   13
s002         13.0   12   14
s003         13.0   13   13
s004         12.0   12   12

"""

