# Javier Vazquez
# Grid Printer
# Date
# Description:

import os

def line(x):
    '''a very simple straight horizontal line at y = 5'''
    return 5

def area(x):
    return ((x[len(x)-1]-x[0])/len(x))*((x[0]+x[len(x)-1])/2+sum(x[1:99]))

def quadratic(x, A=0, B=0, C=0):
    return A * x**2 + B * x + C


def trapz(fun, a, b, A=0, B=0, C=0):
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
    n = 100
    interval = (b-a)/n
    aux = [a if i == 0 else b if i == 99 else interval*i for i in range(n)]
    return fun(aux)
    # return fun(b-a, A, B, C)

def main():
    result = trapz(area, 0, 10)
    print(result)
    # result = trapz(quadratic, 2, 20, A=1, B=3, C=2)
    # print(result)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()