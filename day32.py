
# DAY 32: Set Methods in Python

# Defining sample sets
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# 1. Union and Update
# union() returns a new set; update() modifies the original set inline
print("--- 1. Union & Update ---")
print("Union:", s1.union(s2)) 

s1.update(s2)
print("s1 after update(s2):", s1) # s1 now contains elements of both


# 2. Intersection and Intersection Update
# intersection() returns common elements; intersection_update() modifies inline
print("\n--- 2. Intersection ---")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.intersection(cities2)
print("Intersection:", cities3)

cities.intersection_update(cities2)
print("cities after intersection_update:", cities)


# 3. Symmetric Difference
# Returns elements that are NOT in both sets (elements unique to each set)
print("\n--- 3. Symmetric Difference ---")
set_a = {"Tokyo", "Madrid", "Berlin", "Delhi"}
set_b = {"Tokyo", "Seoul", "Kabul", "Madrid"}

set_c = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", set_c) # {'Berlin', 'Delhi', 'Seoul', 'Kabul'}

set_a.symmetric_difference_update(set_b)
print("set_a after symmetric_difference_update:", set_a)


# 4. Difference and Difference Update
# Returns elements present only in the first set and not in the second
print("\n--- 4. Difference ---")
set_x = {"Tokyo", "Madrid", "Berlin", "Delhi"}
set_y = {"Tokyo", "Seoul", "Kabul", "Madrid"}

set_z = set_x.difference(set_y)
print("Difference (set_x - set_y):", set_z) # {'Berlin', 'Delhi'}


# 5. Set Disjoint, Superset, and Subset (Boolean Checks)
print("\n--- 5. Set Relationships ---")
set1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
set2 = {"Seoul", "Kabul"}
set3 = {"Tokyo", "Madrid"}

print("Are set1 and set2 disjoint?:", set1.isdisjoint(set2)) # True (no common items)
print("Is set1 a superset of set3?:", set1.issuperset(set3)) # True
print("Is set3 a subset of set1?:", set3.issubset(set1))     # True


# 6. Adding and Removing Items
print("\n--- 6. Managing Elements ---")
test_set = {"Tokyo", "Madrid", "Berlin", "Delhi"}

# add() inserts a single item
test_set.add("Helsinki")
print("After adding Helsinki:", test_set)

# remove() vs discard()
# remove() throws a KeyError if the item doesn't exist; discard() does not.
test_set.remove("Tokyo") 
test_set.discard("Russia") # Will not raise an error even though 'Russia' isn't there
print("After remove/discard operations:", test_set)

# pop() removes and returns a random element from the set
popped_item = test_set.pop()
print(f"Popped item: {popped_item} | Remaining set: {test_set}")

# clear() empties the set entirely
test_set.clear()
print("After clear():", test_set) # Output: set()

# del completely deletes the set variable from memory
del test_set
# print(test_set) # This would throw a NameError
