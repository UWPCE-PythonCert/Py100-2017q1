
def count_evens(lst):
    """
    Determines the number of even integers in a passed in list of integers
    Example: count_evens([1,2,3,4]) would return 2
    >>> count_evens([1,2,3,4])
    2
    >>>
    """
    cnt = 0
    if not type(lst) is list:
        return 0
    else:
        for x in lst:
            if not type(x) is int:
                pass
            else:
                if x % 2 == 0:
                    cnt += 1
    return cnt

if __name__ == "__main__":
    print(count_evens([2,2,8,4]))