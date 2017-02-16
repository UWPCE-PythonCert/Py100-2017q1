#!/usr/bin/env python3
#Write a function that draws a grid
#http://uwpce-pythoncert.github.io/IntroToPython/exercises/grid_printer.html#exercise-grid-printer

#part 1
cell_size = 4
for cell_count in range(0,2):
    for i in range(0,2):
        print('+','- '*cell_size, end='')
    print('+')

    for j in range(0,cell_size):
        for k in range(0,2):
            print('|','  '*cell_size, end='')
        print('|')

for l in range(0,2):
    print('+','- '*cell_size, end='')
print('+')


#part 2
def print_grid(n):
    cell_size = int((n-1) / 2)
    for cell_count in range(0,2):
        for i in range(0,2):
            print('+','- '*cell_size, end='')
        print('+')

        for j in range(0,cell_size):
            for k in range(0,2):
                print('|','  '*cell_size, end='')
            print('|')

    for l in range(0,2):
        print('+','- '*cell_size, end='')
    print('+')

n = int(input("cell_size: "))
print_grid(n)

#part 3
def print_grid2(c,s):
    for cell_count in range(0,c):
        for i in range(0,c):
            print('+','- '*s, end='')
        print('+')

        for j in range(0,s):
            for k in range(0,c):
                print('|','  '*s, end='')
            print('|')

    for l in range(0,c):
        print('+','- '*s, end='')
    print('+')

c = int(input("cell_count: "))
s = int(input("cell_size: "))

print_grid2(c,s)
