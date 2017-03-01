arabic_library_ones = [
    ('0', ' '),
    ('1', 'I'),
    ('2', 'II'),
    ('3', 'III'),
    ('4', 'IV'),
    ('5', 'V'),
    ('6', 'VI'),
    ('7', 'VII'),
    ('8', 'VIII'),
    ('9', 'IX'),

]
arabic_library_tens = [
    ('1', 'X'),
   # ('11', 'XI'),
    ('2', 'XX'),
   # ('22', 'XII'),
    ('3', 'XXX'),
    ('4', 'XL'),
    ('5', 'L'),
    ('6', 'LX'),
    ('7', 'LXX'),
    ('8', 'LXXX'),
    ('9', 'XC'),
    ('10', 'C'),
]

roman_library_ones = [
    ('I', '1'),
    ('II', '2'),
    ('III', '3'),
    ('IV', '4'),
    ('V', '5'),
    ('VI', '6'),
    ('VII', '7'),
    ('VIII', '8'),
    ('IX', '9'),

]

roman_library_tens = [
    ('X', '1'),
    ('XX', '2'),
    ('XXX', '3'),
    ('XL', '4'),
    ('L', '5'),
    ('LX', '6'),
    ('LXX', '7'),
    ('LXXX', '8'),
    ('IC', '9')
]


class converter():

    def numeral_validator(self, numeral):
        # Checking that the numeral can reasonably be converted.
        # If it passes validation, then it will run the numeral through the appropriate converter.

        # Checking for negative numbers.
        if numeral[0] is "-":
            print(Exception("You have entered a numeral lower than 1. Don't do that. Restarting...\n"))
            return
        # Checking for decimals.
        if "." in numeral:
            try:
                int(numeral) % 1 == 0
            except ValueError as error:
                print("You must enter a whole number. No decimals allowed. Restarting...\n".format(error))
                return
        # Checking for nonzero integer.
        if numeral == "0":
            print("You must enter a number greater than 0. Restarting...\n")
            return
        # Checking whether starting numeral is Arabic or Roman.
        # If the numeral is Arabic (isdigit()), we've already validated, so we can just pass it to the converter.
        if numeral.isdigit():
            self.arabic_to_roman(numeral)
        elif type(numeral) == str:
            # Additional validation for Roman numerals only.
            for letter in numeral:
                if letter in ['I', 'V', 'X', 'L', 'C']:
                    continue
                else:
                    print("You've entered in an invalid Roman numeral or Arabic numeral. Restarting...")
                    return
            self.roman_to_arabic(numeral)

    def arabic_to_roman(self, numeral):
        print("\nIt appears you have entered an Arabic numeral. Converting to Roman numeral...")
        roman_numerals = []
        if len(numeral) == 1:
            for key, value in arabic_library_ones:
                if numeral[-1] == key:
                    roman_numerals.append(value)
                    continue
        else:
            for key, value in arabic_library_tens:
                if numeral[0] == key:
                    roman_numerals.append(value)
                    break
            for key, value in arabic_library_ones:
                if numeral[1] == key:
                    roman_numerals.append(value)
                    break



        print("Your Roman numeral is: {}".format(''.join([str(item) for item in roman_numerals])))

    def roman_to_arabic(self, numeral):
        print("\nIt appears you have entered an Roman numeral. Converting to Arabic numeral...")
        arabic_numerals = []
        translation_counter = 0
        for key, value in reversed(roman_library_tens):
            if numeral[0] == key or numeral[0:1] == key or numeral[0:2] == key:
                numeral = numeral.replace(key, "")
                arabic_numerals.append(value)
        for key, value in roman_library_ones:
            if numeral == key:
                numeral.replace(key, "")
                arabic_numerals.append(value)
                translation_counter += 1
                break

        if translation_counter == 0:
            arabic_numerals.append('0')



        print("Your Arabic numeral is: {}".format(''.join([str(item) for item in arabic_numerals])))

    def main(self):
        numeral = input("\nWelcome to the Roman/Arabic Numeral Converter. \n\nPlease enter the value to be converted: ")
        self.numeral_validator(numeral)

    def __init__(self):
        while True:
            self.main()

if __name__ == "__main__":
    converter()
