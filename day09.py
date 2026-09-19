
# DAY 9: TYPECASTING  (EXPLICIT & IMPLICIT TYPECASTING) 

# --- EXPLICIT TYPECASTING ---
string = "15"
number = 7
# Explicitly converting string to integer
string_number = int(string) 
sum_result = number + string_number
print("The Sum of both the numbers is:", sum_result)


# --- IMPLICIT TYPECASTING ---
a = 7
print(type(a))
b = 3.0
print(type(b))
# Python automatically converts 'a' to a float type
c = a + b
print(c)
print(type(c))


# =========================================================
# 🖥️ EXPECTED PROGRAM OUTPUT:
# =========================================================
# The Sum of both the numbers is: 22
# <class 'int'>
# <class 'float'>
# 10.0
# <class 'float'>
# =========================================================
