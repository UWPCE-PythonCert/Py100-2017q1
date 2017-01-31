# Javier Vazquez
# Grid Printer
# Jan 30, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/string_formatting.html

import os

def main(*args):
    '''String formatting'''
    print("file_00{0} :   {1:<3.2f}, {2:<.0e}".format(*args))

if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main(2, 123.4567, 10000)