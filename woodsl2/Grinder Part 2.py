#Part 2

#grind function
def print_grind(n):
    x=int(n/2)
#print out horizontal top.
    print('+' + x*'-' + '+' + x*'-' + '+')
    for i in range(x):
#print out vertical
        print('+' + x*' ' + '|' + x*' ' + '|')
#print out horizontal bottom.
    print('+' + x*'-' + '+' + x*'-' + '+')
#calling the function print_grind(n)
print_grind(3)
##for line break or space
print()
#calling function priunt_grind(15)
##for line break or space
print()
