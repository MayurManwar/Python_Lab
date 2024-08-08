import pandas as pd
import matplotlib.pyplot as plt

# Define the DataFrame
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group by 'class' and count the number of students in each class
class_counts = student_data.groupby('class').size()

# Display the counts
print("Number of students in each class:")
print(class_counts)

# Plot the results as a bar chart
class_counts.plot(kind='bar', color='skyblue')

# Add labels and title
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.title('Number of Students by Class')

# Display the bar chart
plt.show()


"""
output

Number of students in each class:
class
V     2
VI    4
dtype: int64

"""

