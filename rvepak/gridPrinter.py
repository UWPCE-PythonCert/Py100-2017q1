import sys
import argparse

parser = argparse.ArgumentParser(
    description='This is a script to generate gridPrinter')
parser.add_argument('-r', help='rowsColumns', required=True)
parser.add_argument('-v', help='verticals', required=True)
args = parser.parse_args()

rowsColumns = args.r
verticals = args.v


def print_grid2(r, v):
    '''
  this method takes arguments as r -- number of rows and
  v-- number of columns.
  '''

    r = round(float(r))
    v = round(float(v))
    print('Creating grids for {} and {}'.format(r, v))
    horizontalLine = '+' + '-' * (v)
    verticalLine = '|' + ' ' * (v)

    rowCounter = 0
    while rowCounter < r:
        print(horizontalLine * r + '+')
        for i in range(0, v):
            print(verticalLine * (r + 1))
        rowCounter += 1
    print(horizontalLine * r + '+')


print(type(rowsColumns))
print_grid2(rowsColumns, verticals)
