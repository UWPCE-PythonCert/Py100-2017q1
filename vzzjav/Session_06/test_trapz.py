# Javier Vazquez
# Grid Printer
# Date
# Description:

import os

def line(x):
    '''a very simple straight horizontal line at y = 5'''
    return 5

def area(x):
    n = 100
    interval = x/n
    aux = []
    for i in range(n):
        if i == 0:
            aux.append(interval)
        elif i == 99:
            aux.append(interval)
        else:
            aux.append(interval)
    return sum(aux)


def trapz(fun, a, b):
    """
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for teh integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value
    """

    return fun(b-a)

def main():
    result = trapz(area, 0, 10)
    print(result)



if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()