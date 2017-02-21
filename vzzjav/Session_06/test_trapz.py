# Javier Vazquez
# Grid Printer
# Date
# Description:

import os

def line(x):
    '''a very simple straight horizontal line at y = 5'''
    return 5

def trapz(fun, a, b, n=100):
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
    increase = (b-a)/n
    print(increase)
    print("hola")
    increment = a
    print(increment)
    while increment < b:
        increment += increase
        print(increment)
    return (b-a)*fun

def main():
    area = trapz(line(0), 0, 10)
    print(area)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()