
def fibonacci(n):
    """Return fibonacci series."""
    if type(n) != int:
        print("n must be an integer!")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(10))


def lucas(n):
    """Return fibonacci series."""
    if type(n) != int:
        print("n must be an integer!")
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

print(lucas(10))


def sum_series(n, val1=0, val2=1):
    """Return a series."""
    if type(n) != int:
        print("n must be an integer!")
    elif n == 0:
        return val1
    elif n == 1:
        return val2
    else:
        return sum_series(n-2) + sum_series(n-1)

# ERROR: This does not produce Lucas number.
print(sum_series(10, 2, 1))
