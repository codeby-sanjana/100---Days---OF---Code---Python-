#Day25: Manipulating Tuples

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item
temp.pop(3)                 # remove item
temp[2] = "Finland"         # change item
countries = tuple(temp)
print(countries)

countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "China", "Japan")
southAsia = countries1 + countries2
print(southAsia)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 32, 3, 1)
res = tuple1.count(1)
# res = tuple1.index(3)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 1 in tuple1 is:', res)
