li = list()  # creating a empty list using constructor
print(dir(li))  # seeing all functionality using dir:

# add single value to end of the array:
li.append(1)

# add single value with specific position:
# That means 1 number index e 2 add koro:
li.insert(1, 2)

# remove to the value from the array:
li.remove(2)

li.append(2)
li.append(3)
li.append(4)
li.append(5)

# remove to the last value from the array:

li.pop()

# remove the specific index using pop:
li.pop(3)

# seeing the length of the array:
print(len(li))


print(li)
