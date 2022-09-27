from tokenize import Double


def double(x): return x*2


print(double(4))


# lambda function and it is also called an anonymous function:

# using map and lambda:
numbers = [1, 2, 3, 4, 5]
double_numbers = list(map(lambda x: x*2, numbers))
print(double_numbers)


# using filter and lambda:
even_numbers = list(filter(lambda x:x%2==0,numbers))
print(even_numbers)
