import numeral_converter

# Test if input of arabic 1 == roman I
def test1():
    # Returns the roman numeral
    roman_out = numeral_converter.numeral()
    roman_out.arabic_numeral = 1
    roman_result = roman_out.get_roman()

    # Returns the arabic numeral from the given roman numeral
    arabic_out = numeral_converter.numeral()
    arabic_out.roman_numeral = str(roman_out.get_roman())
    arabic_result = arabic_out.get_arabic()

    assert roman_result == arabic_result

# Test if input of arabic 4 == roman IV
def test2():
    # Returns the roman numeral
    roman_out = numeral_converter.numeral()
    roman_out.arabic_numeral = 4
    roman_result = roman_out.get_roman()

    # Returns the arabic numeral from the given roman numeral
    arabic_out = numeral_converter.numeral()
    arabic_out.roman_numeral = str(roman_out.get_roman())
    arabic_result = arabic_out.get_arabic()

    assert roman_result == arabic_result

# Test if roman CL == arabic 150
def test3():
    # Returns the arabic numeral for the given roman numeral
    arabic_out = numeral_converter.numeral()
    arabic_out.roman_numeral = str('CL')
    arabic_result = arabic_out.get_arabic()

    # Prints the roman numeral for the given arabic numeral
    roman_out = numeral_converter.numeral()
    roman_out.arabic_numeral = arabic_out.arabic_numeral
    roman_result = roman_out.get_roman()

    assert roman_result == arabic_result

# Test if roman MCMXCIX == arabic 1999
def test4():
    # Returns the arabic numeral for the given roman numeral
    arabic_out = numeral_converter.numeral()
    arabic_out.roman_numeral = str('MCMXCIX')
    arabic_result = arabic_out.get_arabic()

    # Prints the roman numeral for the given arabic numeral
    roman_out = numeral_converter.numeral()
    roman_out.arabic_numeral = arabic_out.arabic_numeral
    roman_result = roman_out.get_roman()

    assert roman_result == arabic_result
