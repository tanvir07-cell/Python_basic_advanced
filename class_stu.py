class Student:

    '''
      Lab Task 04
      id : 202-15-14402
      Name : "Tanvir Rifat"
      sec : 58(New_B)
    '''

    def __init__(self, name, id):
        self._name = name  # protected value
        self._id = id  # protected value

    def __private_method(self):
        print("This is the private Method")


print("stu1_details:")
print("stu_1 is a student")
std1 = Student("Tanvir Rifat", 21)
print(f'Name is {std1._name}')
print(f'Id is {std1._id}')


# for printing docString:
print(Student.__doc__)
