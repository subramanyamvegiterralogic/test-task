li = [x for x in range(1,232,13)]
print(li)
def factorial(n):
    if n == 0:
        return 1
    else:
        res = n*factorial(n-1)
    return res
# print(factorial(5))

def lambda_filter():
    l = list(filter(lambda x:x%4 != 0,li))
    print(l)
# lambda_filter()


def lambda_map():
    l = list(map(lambda item:item//3,li))
    print(l)
# lambda_map()

import functools
def lambda_reduce():
    l = functools.reduce(lambda x,y:x+y,li)
    print(l)
# lambda_reduce()

def function_aliasing(name):
    print('Hi Mr.{}'.format(name))
fun_alias = function_aliasing
print(id(fun_alias))
print(id(function_aliasing))
fun_alias('Subramanyam Vegi')
function_aliasing('Vegi Subramanyam')
del function_aliasing
fun_alias('Terralogic Software Solutions')

