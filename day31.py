
# DAY 31: Sets in Python


# 1. Creating a Set and Automatic De-duplication
# Sets remove duplicate values and do not maintain order
s = {2, 4, 2, 6, 1, 1, 5}
print("De-duplicated Set:", s) 
# Output will look similar to: {1, 2, 4, 5, 6}

info = {"Carla", 19, False, 5.9, 19}
print("Mixed Set without duplicate 19:", info)
# Output removes the second 19: {False, 'Carla', 19, 5.9}


# 2. The Empty Set Catch
# An empty {} creates a dictionary. You must use set() for an empty set.
sanjana = {}
print("Type of sanjana {}:", type(sanjana))  # Output: <class 'dict'>

sanjana_set = set()
print("Type of sanjana_set set():", type(sanjana_set))  # Output: <class 'set'>


# 3. Accessing Set Items using a loop
# Since sets are unordered, you cannot use index numbers like s[0].
# You must access the values using a 'for' loop.
print("\nIterating through the set elements:")
for value in info:
    print("-", value)
