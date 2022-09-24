a = 6
b = 6

# Here a and b both are same. Because a's id and b's id both are same
print(id(a))
print(id(b))
print(a is b)


arr1 = ["Tanvir Rifat", 123]
arr2 = ["Tanvir Rifat", 123]
# Here arr1 and arr2's are not same because this memory location are not same:
print(id(arr1))
print(id(arr2))

a1 = 10
a1 = 20
print(a1)

print(0b0010101)

print((8 < 9) == True)
