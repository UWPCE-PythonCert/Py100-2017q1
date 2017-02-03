

def fizzbizz(lst):
    """
    Simple error checking
    Takes a list as an argument
    Numbers that are divisable by 3 are replaced by FIZZ
    Numbers that are divisable by 5 are replaced by BIZZ
    Numbers that are divisable by 3 & 5 are replaced by FIZZBIZZ
    >>> fizzbizz([x for x in range(1,16)])
    [1, 2, 'FIZZ', 4, 'BIZZ', 'FIZZ', 7, 8, 'FIZZ', 'BIZZ', 11, 'FIZZ', 13, 14, 'FIZZBIZZ']
    """
    # Test for a valid lst
    if not type(lst) is list:
        return None
    # Replace divisable by 3 & 5
    for x in lst:
        if x % 3 == 0 and x % 5 == 0:
            lst[x-1] = "FIZZBIZZ"
    # Replace divisable by 3
    for x in lst:
        if type(x) is int:
            if x % 3 == 0:
                lst[x-1] = "FIZZ"
    # Replace divisable by 5
    for x in lst:
        if type(x) is int:
            if x % 5 == 0:
                lst[x-1] = "BIZZ"
    
    return lst
    
if __name__ == "__main__":
    print(fizzbizz([x for x in range(1,101)]))