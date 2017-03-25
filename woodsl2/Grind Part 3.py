
def print_grind2(m,n):
    x=int(n)
    y=int(m)
    for i in range(y):
        print(y*('+'+ x*'-')+'+')
        for j in range(x):
            print((y+1)*('|'+ (x)*' '))
    print(y*('+' + x*'-')+'+')
#calling the grind2 function
print_grind2(3, 4)
##for line break or space
print()
##calling function
print_grind2(5,3)
##for line break
print()