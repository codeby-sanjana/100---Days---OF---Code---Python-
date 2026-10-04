
#  DAY 24: Introduction to Tuples in Python


tup = (1, 2, 76, 342, 32, "Green", True)
print(type(tup), tup)

# Crucial Edge Case: A tuple with a single element must have a trailing comma
tup_single_wrong = (1)   # Python will treat this as an Integer!
tup_single_right = (1,)  # This is correctly recognized as a Tuple
print("Wrong single element type:", type(tup_single_wrong))
print("Right single element type:", type(tup_single_right))

  
print("Element at index 0:", tup[0])
print("Element at index 2:", tup[2])
print("Element at index 5:", tup[5])

print("Element at index -1:", tup[-1]) 


if 342 in tup:
    print("Yes, 342 is present in this tuple.")
else:
    print("No, it is not present.")


tup2 = tup[1:4]
print("Sliced Tuple (indices 1 to 3):", tup2)

tup3 = tup[0:6:2]
print("Sliced Tuple with jump of 2:  ", tup3)
