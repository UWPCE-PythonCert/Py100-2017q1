#!/usr/bin/env python3

"""Program to convert to and from Roman numerals."""

from roman_class import *


def main():
    """Main function for roman numeral conversion program."""

    # Create instance of the ToFromRoman class.
    converter = ToFromRoman()

    while True:
        try:
            integer = input("Enter a number to convert to"
                            " Roman numeral: ")
            converted = converter.to_roman(integer)

            break

        except ValueError:
            print("Bad value! Please enter integer number only")

            continue

        except OutOfRange:
            print("Out of range! Enter number between 1 and 4999.")

    print("Arabic number {} in roman numerals is {}".format(integer,
                                                            converted))

    while True:
        try:
            romnum = input("Enter a Roman numeral to convert to"
                           " Arabic: ")
            converted = converter.to_arabic(romnum)

            break

        except LimitViolation:
            print("Bad Roman numeral! Too many repeated values!")

            continue

        except BadCharacters:
            print("Bad Roman numeral! Invalid or unknown characters!")

    print("Roman numeral {} in Arabic  is {}".format(romnum,
                                                     converted))

if __name__ == '__main__':
    main()
