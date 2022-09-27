x = "global"


def func():
    global x
    x = x*2
    print(x)


func()
