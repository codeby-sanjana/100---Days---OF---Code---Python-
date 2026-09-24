# Day 14:  Conditional Statements in Python

# 1. Simple if-else Block

user_age = int(input("Enter your current age: "))
print("Your entered age is:", user_age)

# Conditional operator checks: >, <, >=, <=, ==, !=
if user_age >= 18:
    print("Status: You are eligible to vote.")
else:
    print("Status: You are a minor. Voting is not allowed.")

print("Note: This line runs regardless of the condition because it is outside the block.")

# 2. if-elif-else Ladder (Multiple Conditions)

item_price = int(input("Enter product price: "))
budget = 200

if budget - item_price > 50:
    print("Deal: Great buy! You save a good amount of money.")
elif budget - item_price >= 0:
    print("Deal: Affordable, but it consumes most of your budget.")
else:
    print("Deal: Transaction declined. This item exceeds your budget limit.")



# 3. Nested if-else Statements (Conditions Inside Conditions)
#
target_number = int(input("Enter an integer to evaluate: "))

if target_number < 0:
    print("The number is Negative.")
elif target_number > 0:
    print("The number is Positive.")
    
    # Nested check inside the positive number branch
    if target_number <= 10:
        print("Range: The number is between 1 and 10.")
    elif target_number > 10 and target_number <= 50:
        print("Range: The number is between 11 and 50.")
    else:
        print("Range: The number is greater than 50.")
else:
    print("The number is exactly Zero.")
