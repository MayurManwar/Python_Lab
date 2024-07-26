
# Calculate the total revenue generated by two product categories in a store 

import numpy as np

# Revenue arrays
category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate total revenue
total_revenue = category1_revenue + category2_revenue

print("Total Revenue:", total_revenue)

"""
OUTPUT

Total Revenue: [ 950 1300 1500 1150]
"""
