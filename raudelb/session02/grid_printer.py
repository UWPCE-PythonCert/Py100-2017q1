__author__ = 'raudel'


def print_grid2(a, b):
    b += 1
    l = a*(a-1) + 1
    for i in range(l):
        line = ''
        for j in range(l):
            r_y = i % b
            r_x = j % b
            if not r_x and not r_y:
                line += '+'
            elif r_x and not r_y:
                line += '-'
            elif not r_x and r_y:
                line += '|'
            elif r_x and r_y:
                line += ' '
        print(line)


print_grid2(5, 3)
