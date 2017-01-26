for n in range(1,101):
    output = str(n) + ""
    if n%4==0 and n%5==0:
        output = output + " - Fizzbuzz"
    elif n%4==0:
        output = output + " - Fizz"
    elif n%5==0:
        output = output + " - Buzz"
    print(output)
