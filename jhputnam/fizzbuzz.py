#!/usr/bin/env python3

"""Example of the classic fizzbuzz problem."""


def fizzbuzz(number):
    """
    Function for classic fizzbuzz test.
    Arguments:
    number -- The range of numbers to use for fizzbuzzing
    """

    position = 1
    while position <= number:
        if position % 3 == 0 and position % 5 == 0:
            print("FizzBuzz")
        elif position % 3 == 0:
            print("Fizz")
        elif position % 5 == 0:
            print("Buzz")
        else:
            print(position)
        position += 1


def get_number():
    """
    Function to ask the user for a number.
    """

    while True:
        try:
            number = int(input("Enter an integer value for use as a range for"
                               " fizzbuzz: "))
        except ValueError:
            print("Not a standard int. Please try again.")
            continue
        else:
            break

    return number


def main():
    """
    Main entry point for the program.
    """

    number = get_number()
    fizzbuzz(number)


if __name__ == '__main__':
    main()
