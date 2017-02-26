class ConvertRomanArabic:
    roman_numbers = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    roman_ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

    # def __init__(self):

    def arabic_to_roman(self, arabic_number):
        roman_number = []
        for i in range(len(self.roman_ints)):
            total = int(arabic_number / self.roman_ints[i])
            roman_number.append(self.roman_numbers[i] * total)
            arabic_number -= self.roman_ints[i] * total
        return ''.join(roman_number)

    def roman_to_arabic(self, roman_num):
        return None


print(ConvertRomanArabic().arabic_to_roman(999))
