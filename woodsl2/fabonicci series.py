# function fabonicci series

def fabonicci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonicci(n - 1) + fabonicci(n - 2)


# function for lucus series
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


# function for lucus series

# function for sum series which works as fabonicci
# or lucus based on the optimal parameters

def sum_series(n, x=0, y=1):
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 1, x, y)

## testing

## fabonicci series:
assert (fabonicci(0) == 0)
assert (fabonicci(1) == 1)
assert (fabonicci(2) == 1)
assert (fabonicci(3) == 2)
assert (fabonicci(4) == 3)
assert (fabonicci(5) == 5)
assert (fabonicci(6) == 8)
assert (fabonicci(7) == 13)
## lucas series:
assert (lucas(0) == 2)
assert (lucas(1) == 1)
assert (lucas(2) == 3)
assert (lucas(3) == 4)
assert (lucas(4) == 7)
assert (lucas(5) == 11)
assert (lucas(6) == 18)
assert (lucas(7) == 29)
