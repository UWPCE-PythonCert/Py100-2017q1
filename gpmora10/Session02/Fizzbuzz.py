def fizzbuzz(size, fizz = 3, buzz = 5):
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
    return results

fizz1 = fizzbuzz()
fizz2 = fizzbuzz(128,3,5)
assert fizz1 == fizz2, "Error message"
