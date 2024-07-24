
#Compute the median of the flattened NumPy array

import numpy as np

#creating 1 D array with odd no of element
odd_arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("\n Original array : ")
print(odd_arr)

#calculate median
median_Of_arr = np.median(odd_arr)
print("\nMedian of odd Element Array" )
print(median_Of_arr)

"""

 Original array : 
[1 2 3 4 5 6 7]

Median of odd Element Array
4.0

""