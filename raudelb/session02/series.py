__author__ = 'raudel'


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

fib = []
for i in range(0,10):
    fib.append(fibonacci(i))

print(fib)