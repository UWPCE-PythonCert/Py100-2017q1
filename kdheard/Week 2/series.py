def fibonacci(n):
    val1 = 1
    val2 = 1
    for i in range (0, int(n)):
        if i == 0:
            print(0)
        elif i == 1:
            print(1)
        elif i >= 2:
            total = val1 + val2
            print(total)
            val1 = val2
            val2 = total


fibonacci(6)