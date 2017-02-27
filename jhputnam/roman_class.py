#!/usr/bin/env/python3

"""Module for converting to and from Roman numerals."""


class OutOfRange(Exception):
    """Custom exception for out of range."""

    pass


class LimitViolation(Exception):
    """Custom exception for violations of roman numeral repeat limit."""

    pass


class BadCharacters(Exception):
    """Custom exception for bad or unkown characters."""

    pass


class ToFromRoman:
    """Class to handle the conversion between Arabic and Roman numerals."""

    def __init__(self):
        """Init class with instance vars unique to each instance."""

        self.numerals = tuple(zip(
            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV',
             'I'),
            (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
            (3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3)))

    def to_roman(self, arabic):
        """
        Class method to take an Arabic numeral and convert it to a Roman
        numeral.

        Args:
            arabic: Arabic integer numeral to convert to Roman numeral.

        Returns:
            A string containing the Roman numeral representation of the Arabic
            numeral given.

        Raises:
            ValueError: Raised when input is not able to convert to integer.
            OutOfRange: Raised when input is not between 1 and 3999.
        """

        # Validate the input.
        try:
            arabic = int(arabic)

        except ValueError:
            raise

        if arabic not in range(1, 3999):
            raise OutOfRange("Out of range! Valid range: 1-3999")

        # Do the conversion.
        result = []
        for numeral, integer, _ in self.numerals:
            count = arabic // integer
            result.append(numeral * count)
            arabic -= integer * count

        return ''.join(result)

    def to_arabic(self, roman):
        """
        Class method to take a Roman numeral and convert it to an Arabic
        numeral.

        Args:
            roman: Roman numeral to convert to Arabic numeral.

        Returns:
            A string containing the Arabic numeral representation of the Roman
            numeral given.

        Raises:
            LimitViolation: Raised when a particular Roman numeral is repeated
                            too many times.
            BadCharacters: Raised when input contains unknown/invalid
                           characters.
        """

        # Force uppercase.
        roman = roman.upper()

        idx = conversion = 0
        for numeral, integer, maxnum in self.numerals:
            count = 0

            while roman[idx: idx + len(numeral)] == numeral:
                count += 1

                # Check for violation of Roman numeral repeat limit.
                if count > maxnum:
                    raise LimitViolation("Invalid Roman numeral! Too many"
                                         " repetitions!")

                conversion += integer
                idx += len(numeral)

        # Validate for unexpected/unknown characters.
        if idx < len(roman):
            raise BadCharacters("Invalid input! Bad or unknown characters"
                                " detected!")
        else:
            return conversion
