
#Calculate the profit made by a company

import numpy as np

# Revenue and expenses arrays
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate profit
profit = revenue - expenses

print("profit made by a company:", profit)

"""
OUTPUT 
profit made by a company:  [6000 7000 6500 5700]

"""
