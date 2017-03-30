# for i in range(0,11):
#     if i in(0,5,10):
#         print ("+----+----+")
#     else:
#         print("|    |    |")


def print_grid2 (numSquares, numDash):
    i=0
    str1=''
    str2=''
    while i <= numSquares:
        if (i != 0):
            str1 += ' '
            str2 += ' '
        str1 += '+'
        str2 += '|'
        j = 0
        while (i != numSquares) and (j < numDash):
            str1 += ' -'
            str2 += '  '
            j+=1
        i+=1
    for i in range(0,numSquares):
        for j in range(0,numDash+1):
            if j==0:
                print(str1)
            else:
                print(str2)
    print(str1)



print_grid2(3,4)


