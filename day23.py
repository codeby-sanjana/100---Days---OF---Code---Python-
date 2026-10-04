
#  DAY 23: List Methods 

# Initial sample lists
l = [11, 45, 1, 2, 4, 6, 1, 1]
print("Original List l:", l)

# 1. append() - Adds an element to the very end of the list
l.append(7)
print("After append(7):", l)

# 2. sort() - Sorts the list in ascending order
l.sort()
print("After sort():   ", l)

# Sort in descending order (highest to lowest)
l.sort(reverse=True)
print("After sort(reverse=True):", l)

# 3. reverse() - Reverses the current order of the list items
l = [11, 45, 1, 2, 4, 6]
l.reverse()
print("After reverse():", l)

# 4. index() - Returns the index position of the first occurrence of a value

print("Index of number 1:", l.index(1))

# 5. count() - Counts how many times a value appears in the list
l_count = [11, 45, 1, 2, 4, 6, 1, 1]
print("Count of number 1:", l_count.count(1))

# 6. copy() - Creates a safe duplicate copy of the list

#
m = l.copy()
m[0] = 0
print("Original l (safely unchanged):", l)
print("Copied and modified m:        ", m)

# 7. insert() - Adds an element at a chosen index position index(index, value)
l.insert(1, 899)  # Inserts 899 right at index 1
print("After insert(1, 899):", l)

# 8. extend() - Appends an entire iterable/list to the end of your list
m_list = [900, 1000, 1100]
l.extend(m_list)
print("After extend(m_list):", l)

# Alternative to extend: Concatenating two lists using '+'
k = l + m_list
print("Concatenated list k (l + m_list):", k)
