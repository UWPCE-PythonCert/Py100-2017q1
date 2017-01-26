# Javier Vazquez
# Grid Printer
# Jan 23, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/fizz_buzz.html

def main():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    main()