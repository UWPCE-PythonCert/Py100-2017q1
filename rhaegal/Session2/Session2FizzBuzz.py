def fizzbuzz(size=100,fizz=3,buzz=5):
    for count in range(1,101):
        printvalue=""
        if count%fizz==0:
            printvalue+="Fizz"
        if count%buzz==0:
            printvalue+="Buzz"
        if (count%fizz!=0) and (count%buzz!=0):
            print(count)
        else:
            print(printvalue)

fizzbuzz()
