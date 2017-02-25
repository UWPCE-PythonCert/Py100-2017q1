# Write a function that draws a grid

def print_grid_p1(n):
    str1 = '+ - - - - + - - - - +'
    str2 = '|         |         |'

    for val in range(n-1):
        print(str1)
        print(str2)
        print(str2)
        print(str2)
        print(str2)
    print(str1)

#print_grid_p1(3)

def print_grid_p2(n):
    str1 = '+'
    str2 = (n)*'-'
    str3 = '|'
    str4 = (n)*' '

    for val in range(2):

        print(str1 + str2 + str1 + str2 + str1)
        for val in range(n):
            print(str3 + str4 + str3 + str4 +str3)
    print(str1 + str2 + str1 + str2 + str1)

#print_grid_p2(3)

#print_grid_p2(15)

def print_grid_p3(grid,n):
    str1 = '+'
    str2 = (n)*'-'
    str3 = '|'
    str4 = (n)*' '

    for val in range(grid):

        print(str1 + str2 + str1 + str2 + str1)
        for val in range(n):
            print(str3 + str4 + str3 + str4 +str3)
    print(str1 + str2 + str1 + str2 + str1)

#print_grid_p2(3)

print_grid_p3(3,4)
