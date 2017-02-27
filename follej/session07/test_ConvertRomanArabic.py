#!/usr/bin/env python3
from ConvertRomanArabic import ConvertRomanArabic


def test_arabic_to_roman():
    assert ConvertRomanArabic().arabic_to_roman(999) == 'CMXCIX'
    assert ConvertRomanArabic().arabic_to_roman(1999) == 'MCMXCIX'
    assert ConvertRomanArabic().arabic_to_roman(13) == 'XIII'


def test_roman_to_arabic():
    assert ConvertRomanArabic().roman_to_arabic('IV') == 4
    assert ConvertRomanArabic().roman_to_arabic('MCMXCIX') == 1999


def test_both_conversions():
    assert ConvertRomanArabic().arabic_to_roman(ConvertRomanArabic().roman_to_arabic('MCMXCIX')) == 'MCMXCIX'
    assert ConvertRomanArabic().roman_to_arabic(ConvertRomanArabic().arabic_to_roman(1999)) == 1999
