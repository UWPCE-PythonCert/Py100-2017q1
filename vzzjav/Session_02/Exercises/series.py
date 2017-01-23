# Javier Vazquez
# Grid Printer
# Jan 23, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/fib_and_lucas.html

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

def main():
    serie = ""
    print("Number of iterations must be greater than 0")
    n = input("Number of iterations: ")
    n = int(n)
    if n <= 0:
        print("Number of iterations must be greater than 0")
    else:
        for i in range(n):
            serie += str(fib(i)) + ", "
    print(serie)

if __name__ == '__main__':
    main()