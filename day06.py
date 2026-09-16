# Day 6: Variables and Built-in Data Types

# --- 1. WHAT IS A VARIABLE? ---
# Creating different variables acting as data containers
a = 8
b = True
c = "Sanjana"
d = None

# Checking data types using the type() function
print("--- Checking Basic Types ---")
print(type(a))
print(type(c))


# --- 2. NUMERIC DATA TYPES ---
print("\n--- Numeric Data Types ---")
num1 = 123             # Integer (int)
num2 = 7.349           # Floating-point (float)
num3 = 6 + 2j          # Complex Number (Python uses 'j' instead of 'i')

print("The type of num1 is:", type(num1))
print("The type of num2 is:", type(num2))
print("The type of num3 is:", type(num3))


# --- 3. TEXT & BOOLEAN DATA TYPES ---
print("\n--- Text & Boolean Data Types ---")
str1 = "Hello World!!!" # Text data (str)
bool1 = True           # Boolean data (bool)

print(str1)
print("Boolean Value:", bool1)


# --- 4. SEQUENCED DATA (LIST & TUPLE) ---
print("\n--- Sequenced Data Types ---")

# Lists are ordered, enclosed in [ ], and mutable (can be changed)
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print("List output:")
print(list1)

# Tuples are ordered, enclosed in ( ), and immutable (cannot be changed)
tuple1 = (("Parrot", "sparrow"), ("Lion", "Tiger"))
print("\nTuple output:")
print(tuple1)


# --- 5. MAPPED DATA (DICTIONARY) ---
print("\n--- Mapped Data Type (dict) ---")

# Dictionaries store unordered key:value pairs inside { }
dict1 = {"Name": "Shriya", "age": 20, "canVote": True}
print("Dictionary output:")
print(dict1)

# ----------------------------------------
# 🖥️ EXPECTED SCREEN OUTPUT:
# ----------------------------------------
# --- Checking Basic Types ---
# <class 'int'>
# <class 'str'>
# 
# --- Numeric Data Types ---
# The type of num1 is: <class 'int'>
# The type of num2 is: <class 'float'>
# The type of num3 is: <class 'complex'>
# 
# --- Text & Boolean Data Types ---
# Hello World!!!
# Boolean Value: True
# 
# --- Sequenced Data Types ---
# List output:
# [8, 2.3, [-4, 5], ['apple', 'banana']]
# 
# Tuple output:
# (('Parrot', 'sparrow'), ('Lion', 'Tiger'))
# 
# --- Mapped Data Type (dict) ---
# Dictionary output:
# {'Name': 'Shriya', 'age': 20, 'canVote': True}
# ----------------------------------------
