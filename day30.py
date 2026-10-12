#Day30 : Rescursive
# Calculating Factorial: e.g., 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    # Base Case: factorial of 0 or 1 is always 1
    if (n == 1 or n == 0):
        return 1
    else:
        # Recursive Case: function calling itself
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120
print(factorial(4)) # Output: 24
