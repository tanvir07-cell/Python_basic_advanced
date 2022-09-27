# def greeting(name, msg="How do you do?"):
#     print(f'{name} {msg} there')


# greeting("Tanvir Rifat")


# arbitery function(that means takes all arguments when we called this function using *);

from re import I


def arbitery_func(*names):
    print(names)  # return a tupple of this all names:
    dic = dict()
    i = 0
    for name in names:
        # creating an object
        dic.update({i: name})
        i = i+1
    print(dic)


arbitery_func("Tanvir Rifat", "Hm Nayeem", "Brad traversy")
