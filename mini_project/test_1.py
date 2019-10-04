# x = 10
class A:
    global y
    y=40
    def __init__(self):
        self.x = 40

    def print_x(self):
        y=50
        print(self.x)
        self.x += 30
        print(y)
    print(y)

# a = A()
# a.print_x()
# print(x)
# print(a.x)

def iterable_obj_test():
    x = [x**2 for x in range(0,100,4)]
    my_itr = iter(x)
iterable_obj_test()