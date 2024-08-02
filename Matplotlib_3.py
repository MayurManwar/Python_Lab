
#Create a pie chart to visualize the distribution of your monthly income by source. 


import matplotlib.pyplot as plt

# Market share data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other'] 
monthly_income = [5000, 1500, 1000, 600, 400]

# Colors for each slice
colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightgrey']

# Create a pie chart
plt.pie(monthly_income, labels=income_sources, colors=colors, autopct='%1.1f%%')

# Title
plt.title('Monthly Income')
# Show the pie chart
plt.show()
