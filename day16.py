#Day16: Match Case statement 

x = int(input("Enter the value of x: "))

match x:
    # if x is 0
    case 0:
        print("x is zero")
        
    # if x is 4
    case 4:
        print("x is 4")

    # case with an if-condition (Guard clause)
    case _ if x != 90:
        print(x, "is not 90")
        
    # another case with an if-condition
    case _ if x != 80:
        print(x, "is not 80")
        
    # Default case / Wildcard (like 'else')
    case _:
        print(x)
