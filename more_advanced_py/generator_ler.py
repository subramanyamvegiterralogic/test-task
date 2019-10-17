def fibonacci(limit):
    a,b = 0, 1
    while a<limit:
        yield a
        a, b = b, a+b


for i in fibonacci(5):
    print(i, end=' ')