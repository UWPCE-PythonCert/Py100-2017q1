for count in range(1,101):
    printvalue=""
    if count%3==0:
        printvalue+="Fizz"
    if count%5==0:
        printvalue+="Buzz"
    if (count%3!=0) and (count%5!=0):
        print count
    else:
        print printvalue
