def increment(x):
    return x+1


def double_increment(func):
    def inner(x):
        r = func(x)
        y = r*2
        return r,y
    return inner


@double_increment
def increment(x):
    return x+1


print(increment(2))
print(increment.__closure__)