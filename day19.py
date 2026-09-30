#  DAY 19: Break and Continue Statements 


for i in range(1, 12):
    if(i == 11):
        print("Leaving the loop...")
        break
    print("5 X", i, "=", 5 * i)
    
print("Go out of the loop")



for i in range(1, 12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)
print("Finished checking continue statement\n")


i = 0
while True:
    print(i)
    i = i + 1
    if(i % 5 == 0): 
        print("Loop stopped using break condition")
        break
