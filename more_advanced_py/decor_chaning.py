
def square(func):
    def inner():
        x = func()
        print('Square INNER called\n X value is : ',x)
        return x*x
    return inner


def double(func):
    def inner():
        x = func()
        print('Double INNER called\n X value is : ',x)
        return x*2
    return inner


@double     # This Decorator will execute second
@square     # This Decorator Will execute First
def calculate():
    return 10
# print(calculate())

a=586
b=22265
def global_test():
    a = 1931
    b = 65
    print(a)
    print(b)
    print(globals()['a'])
    print(globals()['b'])
global_test()