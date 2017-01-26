# Write a function that draws a grid

def print_grid(n):
    str1 = '+ - - - - + - - - - +'
    str2 = '|         |         |'

    for val in range(n-1):
        print(str1)
        print(str2)
        print(str2)
        print(str2)
        print(str2)
    print(str1)

print_grid(3)
