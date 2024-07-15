#. Write a Python script to concatenate the following dictionaries to create a new one.



# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary by concatenating the given dictionaries
result = {**dic1, **dic2, **dic3}

# Print the result
print("Expected Result :", result)


"""
= RESTART: C:/Users/Mayur Manwar/Desktop/Python code/Githup_python/Assignment 19.py
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""
