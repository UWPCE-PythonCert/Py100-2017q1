
def has22(lst):

    """
    Test to determine if there are two adjacent 2s in a passed in list
    >>> x = [0, 1, 4, 2, 2, 3]
    >>> has22(x)
    True
    >>>
    >>> y = [0, 1, 2, 3, 4, 5]
    >>> has22(y)
    False
    >>>
    >>> z = "122345"
    >>> has22(z)
    True
    >>>
    """

    # Initialize counter
    cnt = 0

    try:
      # Run through list
      for x in lst:
          if str(x) == "2" and str(lst[cnt + 1]) == "2":
              return True
          cnt += 1
    except:
        return False
          
if __name__ == "__main__":
    var = [1,2,2,3,4,2]
    print(has22(var))
