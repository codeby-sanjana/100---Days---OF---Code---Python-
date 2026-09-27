# Day 17: Introduction to loop
name = "Sanjana"


for i in name:
    print(i)
    if i == "b":
        print("This is something special!")


colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)

    for i in color:
        print(i)
# range(5) will generate numbers from 0 to 4
for k in range(5):
    print(k + 1)

# range(1, 9) will generate numbers from 1 to 8
for k in range(1, 9):
    print(k)

# range(1, 12, 3) starts at 1, increments by 3, up to 11
for k in range(1, 12, 3):
    print(k)
  
