name = "tanvir Rifat"


# seeing all strings methods available in python:
print(dir(name))

# all letters converting to the uppercase
print(name.upper())

# all letters converting to the lowercase:
print(name.lower())

# upperCase only the first letter:
print(name.capitalize())

# slicing the name string:

print(name[0:5])

# split the name string:
print(name.split(" "))

before_join = ["Hello", "Python", "Lover"]
after_join = " ".join(before_join)
print(after_join)
