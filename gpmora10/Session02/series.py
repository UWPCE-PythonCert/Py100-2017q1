'''def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fibonacci(10)'''
'''
def lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return lucas(n-1) + lucas(n-2)

lucas(10)'''


def sum_series(n,first=0, second=1):
    '''Creates a series of numbers by adding the two preceding the numbers and appending that value.
    it will default to the Fibonnaci sequence if first and second are not defined'''
    sequence = [first, second]
    if n == 0:
        print("0")
        return
    for i in range (n-2):
        sequence.append(first+second)
        first, second = second, first+second
    '''print(sequence)'''
    print(sequence[n-1])

def fibonacci(n):
    '''Returns the nth number in the fibonacci sequence'''
    sum_series(n)

def lucas(n):
    ''' returns the nth number in the lucas sequence'''
    sum_series(n,2,1)

sum_series(11)
sum_series(11,2,1)
fibonacci(10)
lucas(10)
