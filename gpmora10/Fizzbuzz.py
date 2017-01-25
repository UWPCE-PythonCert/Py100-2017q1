def fizzbuzz(size = 100, fizz = 3, buzz = 5):
    results = []
    for i in range(1,size+1):
        value = ""
        if i%fizz == 0:
            value += "Fizz"
        if i%buzz == 0:
            value += "Buzz"
        if i%fizz != 0 and i%buzz !=0:
            value += str(i)
        results.append(value)
    print(results)

fizzbuzz(100,3,5)
