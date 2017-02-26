class numeral():
    import math

    def __init__(self):
        self.roman_numeral = [] #This empty list will be appended with roman numerals in digits places
        self.arabic_numeral = 0 #This is an int, we will use this to add values later
        self.arabic_numeral_sum = self.arabic_numeral
        self.thousands = 0
        self.hundreds = 0
        self.tens = 0
        self.fives = 0
        self.ones = 0

    def get_roman(self): # This turns an arabic numeral into a roman numeral

        self.arabic_numeral_sum = self.arabic_numeral
        self.roman_numeral = []

        # The following block appends the roman_numeral list with the appropriate number of numeral markers in the appropriate digits places
        self.roman_numeral.append(int(self.math.floor(self.arabic_numeral_sum / 1000)) * "M")
        self.arabic_numeral_sum -= int(self.math.floor(self.arabic_numeral_sum / 1000))*1000

        self.roman_numeral.append(int(self.math.floor(self.arabic_numeral_sum / 500)) * "D")
        self.arabic_numeral_sum -= int(self.math.floor(self.arabic_numeral_sum / 500)) * 500

        self.roman_numeral.append(int(self.math.floor(self.arabic_numeral_sum / 100)) * "C")
        self.arabic_numeral_sum -= int(self.math.floor(self.arabic_numeral_sum / 100))*100

        self.roman_numeral.append(int(self.math.floor(self.arabic_numeral_sum / 50)) * "L")
        self.arabic_numeral_sum -= int(self.math.floor(self.arabic_numeral_sum / 50)) * 50

        self.roman_numeral.append(int(self.math.floor(self.arabic_numeral_sum / 10)) * "X")
        self.arabic_numeral_sum -= int(self.math.floor(self.arabic_numeral_sum / 10))*10

        self.roman_numeral.append(int(self.math.floor(self.arabic_numeral_sum / 5)) * "V")
        self.arabic_numeral_sum -= int(self.math.floor(self.arabic_numeral_sum / 5))*5

        self.roman_numeral.append(int(self.math.floor(self.arabic_numeral_sum / 1)) * "I")
        self.arabic_numeral_sum -= int(self.math.floor(self.arabic_numeral_sum / 1))*1

        self.roman_numeral = ''.join(self.roman_numeral)

        # This replaces strings with four iterations of a single numeral with the appropriate string
        self.roman_numeral = self.roman_numeral.replace("XIIII","XIV").replace("XVIIII", "XIX").replace("CXXXX", "CXL").replace("CLXXXX", "CXC").replace("MCCCC", "MCD").replace("MDCCCC", "MCM").replace("DCCCC", "CM")

        print(self.roman_numeral)

    def get_arabic(self): # This turns a roman numeral into an arabic numeral

        self.arabic_numeral = 0
        self.roman_numeral = ''.join(self.roman_numeral)

        # This replaces certain roman numeral strings with four iterations of the appropriate string
        self.roman_numeral = self.roman_numeral.replace("XIV","XIIII").replace("XIX", "XVIIII").replace("CXL", "CXXXX").replace("CXC", "CLXXXX").replace("MCD", "MCCCC").replace("MCM", "MDCCCC").replace("CM" ,"DCCCC")

        # Turn the string into a list
        self.roman_numeral = [i for i in self.roman_numeral]

        # For loop to add to self.arabic_numeral_sum based on the strings in the list
        for i in self.roman_numeral:
            if i == 'I':
                self.arabic_numeral_sum += 1
            if i == 'V':
                self.arabic_numeral_sum += 5
            if i == 'X':
                self.arabic_numeral_sum += 10
            if i == 'L':
                self.arabic_numeral_sum += 50
            if i == 'C':
                self.arabic_numeral_sum += 100
            if i == 'D':
                self.arabic_numeral_sum += 500
            if i == 'M':
                self.arabic_numeral_sum += 1000

        self.arabic_numeral = self.arabic_numeral_sum
        print(self.arabic_numeral)

