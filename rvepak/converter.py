import os
import sys
import string

roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Converter(object):
    def __init__(self, numerical, source_numeric_system,
                 destination_numeric_system):
        self.numerical = numerical
        self.source_numeric_system = source_numeric_system
        self.destination_numeric_system = destination_numeric_system

    def roman_identifier(self):
        for item in roman_map.keys():
            if item in self.numerical:
                return 1
        else:
            return 0

    def roman_to_arabic(self):
        if self.roman_identifier() == 1:
            return sum([roman_map[x] for x in self.numerical])
        else:
            return 'Not a roman letter'

    def arabic_to_roman(self):
        if not self.numerical.isdigit():
            print('{} is not a number'.format(self.numerical))
        roman_output = ''
        value_list = sorted(
            {v: k
             for k, v in roman_map.items()}.keys(), reverse=True)
        print(value_list)
        value_map = {v: k for k, v in roman_map.items()}
        value = int(self.numerical)
        for key in value_list:
            if value % key != value:
                roman_output += value_map[key] * int(value / key)
                value = value % key
        return roman_output


convert = Converter('CCVII', 'Roman', 'Arabic')
print(convert.roman_to_arabic())

convert = Converter('1353', 'Arabic', 'Roman')
print(convert.arabic_to_roman())
