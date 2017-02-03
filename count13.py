
def count13(lst):
    """
    Sum all numbers in a passed in list that are less than 13
    >>> count13([1,2,5,7,8,13,15,20])
    23
    >>>
    """
    if not type(lst) is list:
        return 0
    good_lst = [x for x in lst if type(x) is int or type(x) is float]
    return sum([x for x in good_lst if x < 13])

if __name__ == "__main__":
    lst = [1,2,5,7,8,13,15,20]
    print(count13(lst))
    