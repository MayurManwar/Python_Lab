#Compute the standard deviation of the NumPy array


import numpy as np

# Median calculation
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
median_value = np.median(x_odd)
print("Median:", median_value)

# Standard deviation calculation
arr = np.array([20, 2, 7, 1, 34])
std_deviation = np.std(arr)
print("Standard Deviation:", std_deviation)

print("\n More precious with float-32")
print("Standard Deviation:", std_deviation)

print("\n More accuracy with float-64")
print("Standard Deviation:", std_deviation)

"""
Median: 4.0
Standard Deviation: 12.576167937809991

 More precious with float-32
Standard Deviation: 12.576167937809991

 More accuracy with float-64
Standard Deviation: 12.576167937809991


"""
