import sys

rowsColumns = sys.argv[1]
verticals = sys.argv[2]


def print_grid2(r, c):
    '''
  this method takes arguments as r -- number of rows and
  c-- number of columns.
  '''

    r = round(float(r))
    c = round(float(c))
    print('Creating grids for {} and {}'.format(r, c))
    horizontalLine = '+' + '-' * (c)
    verticalLine = '|' + ' ' * (c)

    rowCounter = 0
    while rowCounter < r:
        print(horizontalLine * r + '+')
        for i in range(0, c):
            print(verticalLine * (r + 1))
        rowCounter += 1
    print(horizontalLine * r + '+')


print(type(rowsColumns))
print_grid2(rowsColumns, verticals)
