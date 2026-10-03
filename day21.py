
#  DAY 21: Function Arguments in Python 



def average(a, b=9):
    print("The average is ", (a + b) / 2)

print("--- 1. Default & Required Arguments ---")
average(4)    # Uses a=4 and default b=9
average(4, 6) # Overrides default b, uses a=4 and b=6

average(b=21, a=9) 



def average_multiple(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average of multiple numbers: ", sum / len(numbers))


average_multiple(5, 6, 7, 1)


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname="Buchanan", lname="Barnes", fname="James")
def calculate_return_average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers) 


c = calculate_return_average(5, 6, 7, 1)
print("Returned value stored in c:", c)
