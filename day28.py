
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Sanjana"
print(letter.format(name, country))

letter = "Hey my name is {1} and I am from {0}"
print(letter.format(country, name))


print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")


txt = f"For only {49.9999:.2f} dollars!"
print(txt)

print(f"{2 * 30}")
print(type(f"{2 * 30}"))
