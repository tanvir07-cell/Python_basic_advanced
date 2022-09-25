# tuple is a immutable so that's why we can't update any value in tuple

tup = tuple()  # creating new empty tuple using tuple constructor:
tup = (1, 2, 3, 4, 5, "Tanvir Rifat")
print(tup)

print(dir(tup))
print(len(tup))

# slicing the tuple:
print(tup[0:3])

# concatenate the two tuple:
tup1 = (1, 2, 3, 4)
tup2 = (5, 6, 7, 8)
print(tup1+tup2)

# counting the item 5 in tuple1;
print(tup2.count(5))


# deleting tup1:
del tup1
