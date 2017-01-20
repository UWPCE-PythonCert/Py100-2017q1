
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
