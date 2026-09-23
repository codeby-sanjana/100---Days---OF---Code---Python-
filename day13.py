# Day 13 - String Methods in Python 

# Strings are immutable (cannot be changed in-place)
a = "!!!Sanjana!! !!!!! Sanjana"
print(len(a))  # Returns the length of the string

# 1. Changing Case
print(a.upper())       # Converts all characters to uppercase
print(a.lower())       # Converts all characters to lowercase

# 2. Stripping and Replacing
print(a.rstrip("!"))   # Strips trailing exclamation marks from the right end
print(a.replace("Sanjana", "John"))  # Replaces all occurrences of "Sanjana" with "John"

# 3. Splitting into a List
str2 = "Silver Spoon"
print(str2.split(" ")) # Splits the string at spaces into a list: ['Silver', 'Spoon']

# 4. Alignment & Capitalization
blogHeading = "introduction tO pYtHoN"
print(blogHeading.capitalize())  # Turns the 1st letter capital, rest lowercase

str1 = "Welcome to the Console!!!"
print(str1.center(50))           # Centers string by padding it with 50 spaces
print(len(str1))
print(len(str1.center(50)))

# 5. Counting and Searching
print(a.count("Sanjana"))         # Counts how many times "Sanjana" appears
print(str1.endswith("!!!"))     # Returns True if string ends with "!!!"
print(str1.endswith("to", 4, 10)) # Checks if a specific sliced range ends with "to"

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))        # Searches for string; returns -1 if NOT found
# print(str1.index("ishh"))     # Like find(), but throws an Error if not found

# 6. Content Validation (Returns True or False)
str1 = "WelcomeToTheConsole"
print(str1.isalnum())      # True if alphanumeric (A-Z, a-z, 0-9), no spaces
print(str1.isalpha())      # True if strictly alphabets (A-Z, a-z), no numbers

str1 = "hello world"
print(str1.islower())      # True if all characters are lowercase

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())  # False if it contains hidden characters like \n

# 7. Checking for Whitespace or Titles
str1 = "        "          # Using Spacebar or Tab keys
print(str1.isspace())      # True if string contains ONLY empty spaces

str1 = "World Language"
print(str1.istitle())      # True if the first letter of every word is capitalized

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python")) # True if string begins with "Python"
print(str1.swapcase())           # Flips case: Lowercase becomes upper and vice-versa

str1 = "His name is Dan. Dan is a good boy."
print(str1.title())        # Capitalizes every single word's first letter
