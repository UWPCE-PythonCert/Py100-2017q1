import collections


class ConvertRomanArabic:
    roman_dict = collections.OrderedDict(
        zip(['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'],
            [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]))

    # def __init__(self):

    def arabic_to_roman(self, arabic_number):
        roman_number = []
        for roman_numeral, roman_integer in self.roman_dict.items():
            total = int(arabic_number / roman_integer)
            roman_number.append(roman_numeral * total)
            arabic_number -= roman_integer * total
        return ''.join(roman_number)

    def roman_to_arabic(self, roman_numeral):
        roman_str = str(roman_numeral)
        total = 0
        for i, roman_number in enumerate(roman_str):
            value = self.roman_dict[roman_number]
            if i + 1 < len(roman_str) and self.roman_dict[roman_str[i + 1]] > value:
                total -= value
            else:
                total += value
        return total


print(ConvertRomanArabic().arabic_to_roman(1999))
print(ConvertRomanArabic().roman_to_arabic('III'))
