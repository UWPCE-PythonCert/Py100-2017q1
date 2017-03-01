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
    ('2', 'XX'),
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
    ('XC', '9')
]


class converter():

    def numeral_validator(self, numeral):
        # Checking that the numeral can reasonably be converted.
        # If it passes validation, then it will run the numeral through the appropriate converter.

        # Checking that user entered something.
        if len(numeral) == 0:
            print(Exception("You must enter something. Restarting..."))
            return
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
        # Checking whether starting numeral is Arabic or Roman, and passing to the appropriate converter.
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

        # Checks for length of numeral, so we know whether to check the tens list or the ones list first.
        # If part of the Arabic number matches something in the list, we add the Roman counterpart to a list to print.
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
        # Now to take all the converted Arabic numerals and smush them together...
        print("Your Roman numeral is: {}".format(''.join([str(item) for item in roman_numerals])))

    def roman_to_arabic(self, numeral):
        print("\nIt appears you have entered an Roman numeral. Converting to Arabic numeral...")
        arabic_numerals = []
        translation_counter = 0
        # A Roman numeral can be anywhere from 1-3 digits, so here we slice the first characters of the numeral and
        # compare it against the tens list.
        # If a character has been converted, we take it out of the numeral and put the converted value into a list.
        for key, value in reversed(roman_library_tens):
            if len(numeral) >= 3:
                if numeral[0:3] == key:
                    numeral = numeral.replace(key, "", 1)
                    arabic_numerals.append(value)
            if len(numeral) >= 2:
                if numeral[0:2] == key:
                    numeral = numeral.replace(key, "", 1)
                    arabic_numerals.append(value)
            if len(numeral) != 0:
                if numeral[0] == key:
                    numeral = numeral.replace(key, "", 1)
                    arabic_numerals.append(value)
            else:
                break
        # Now with all the tens out of the way, we compare the remaining character against the ones list.
        # If anything matches with the ones list, we switch on the "translation counter", so we know we don't have
        # to add "0" to the end of the Arabic numeral, like for "10" and "20".
        for key, value in roman_library_ones:
            if numeral == key:
                numeral.replace(key, "")
                arabic_numerals.append(value)
                translation_counter += 1
                break
        # If we made a match with the tens list but not the ones list (i.e. we're translating 10 or 20), we add a 0 to
        # the end of the numeral.
        if translation_counter == 0:
            arabic_numerals.append('0')

        # Now to take all the converted Roman numerals and smush them together...
        print("Your Arabic numeral is: {}".format(''.join([str(item) for item in arabic_numerals])))

    def main(self):
        # Gather the numeral and then run it through the input validator.
        numeral = input("\nWelcome to the Roman/Arabic Numeral Converter. \n\nPlease enter the value to be converted: ")
        self.numeral_validator(numeral)

    def __init__(self):
        while True:
            self.main()

if __name__ == "__main__":
    converter()
