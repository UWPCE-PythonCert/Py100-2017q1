# Javier Vazquez
# Grid Printer
# Jan 23, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/fib_and_lucas.html

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-2) + fib(n-1))

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n-2) + lucas(n-1))

def main():
    serief = ""
    seriel = ""
    print("Number of iterations must be greater than 0")
    n = input("Number of iterations: ")
    n = int(n)
    if n <= 0:
        print("Number of iterations must be greater than 0")
    else:
        print("Fibonacci")
        for i in range(n):
            serief += str(fib(i)) + ", "
        print(serief)

        print("\nLucas")
        for i in range(n):
            seriel += str(lucas(i)) + ", "
        print(seriel)

if __name__ == '__main__':
    main()