numeral_library_ones = {
    "0": " ",
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX"

}
numeral_library_tens = {
    "1": "X",
    "2": "XX",
    "3": "XXX",
    "4": "XL",
    "5": "L",
    "6": "LX",
    "7": "LXX",
    "8": "LXXX",
    "9": "XC",
    "10": "C"

}


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
            print("You must enter a number greater than 0. In ancient Rome, there was no number to represent 0, "
                  "which was interesting because the number 0 had been around in the Babylonian, Mayan, "
                  "and Sumerian numerical systems prior to use of Roman numerals."
                  "\nOh no! You have died from BORING HISTORY LECTURE. Restarting...\n")
            return
        # Checking whether starting numeral is Arabic or Roman.
        # If the numeral is Arabic (isdigit()), we've already validated, so we can just pass it to the converter.
        if numeral.isdigit():
            self.arabic_to_roman(numeral)
        elif type(numeral) == str:
            # Additional validation for Roman numerals only.
            for letter in numeral:
                if any in ['I', 'V', 'X', 'L', 'C']:
                    continue
                else:
                    print("You've entered in an invalid Roman numeral or Arabic numeral. Restarting...")
                    return
            self.roman_to_arabic(numeral)

    def arabic_to_roman(self, numeral):
        print("\nIt appears you have entered an Arabic numeral. Converting to Roman numeral...")
        if len(numeral) >= 1:
            for key, value in numeral_library_ones.items():
                if numeral[-1] == key:
                    numeral = numeral.replace(numeral[-1], value)
                    continue

        if len(numeral) >= 2:
            for key, value in numeral_library_tens.items():
                if numeral[0] == key:
                    numeral = numeral.replace(numeral[0], value)
        print("Your Roman numeral is: {}".format(''.join([str(item) for item in numeral])))

    def roman_to_arabic(self, numeral):
        print("\nIt appears you have entered an Roman numeral. Converting to Arabic numeral...")
        for key, value in numeral_library_ones.items():
            if value in numeral:
                numeral.replace(value, key)

        print("Your Arabic numeral is: {}".format(''.join([str(item) for item in numeral])))

    def main(self):
        numeral = input("\nWelcome to the Roman/Arabic Numeral Converter. \n\nPlease enter the value to be converted: ")
        self.numeral_validator(numeral)

    def __init__(self):
        while True:
            self.main()

if __name__ == "__main__":
    converter()
