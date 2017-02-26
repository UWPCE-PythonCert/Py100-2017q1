#!/usr/bin/env python3
from ConvertRomanArabic import ConvertRomanArabic


def test_arabic_to_roman():
    assert ConvertRomanArabic().arabic_to_roman(999) == 'CMXCIX'


def test_roman_to_arabic():
    assert ConvertRomanArabic.roman_to_arabic('IV') == 4
