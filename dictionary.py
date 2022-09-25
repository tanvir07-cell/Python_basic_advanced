
dic = dict()  # creating a new dictionary using dict() constructor:


dic = {
    "name": "Tanvir Rifat",
    "id": "202-15-14402",
    1: "This is the number key"
}

# get all elements:
print(dic.items())

# get values:
print(dic.values())

# get keys:
print(dic.keys())

# update the properties:
dic['name'] = "Tanvir Hassan Rifat"

# also using the update method:
dic.update({'name': "Tanvir Rifat(updated)"})

print(dic)
