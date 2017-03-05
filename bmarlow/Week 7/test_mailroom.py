#!/usr/bin/env python

from mailroom import mailroom

donors = {
    'Ricky': [1000],
    'Bobby': [1100, 2200],
    'Hansel': [5000, 6000, 7000],
    'Mr. Burgandy': [1, 2, 3, 4],
    'Austin': [123, 4567, 78, 99, 100],
    'Dale': [14, 234, 878, 345, 345, 234],
}

def test_1():
    assert mailroom.namecheck('Ricky') is True

def test_2 ():
    assert mailroom.namecheck('asdf') is False

def test_3 ():
    assert mailroom.createnewname('TestGuy') == ['Ricky', 'Bobby', 'Hansel', 'Mr. Burgandy', 'Austin', 'Dale', 'TestGuy']

def test_4 ():
    assert mailroom.getdonations('Dale') == [14, 234, 878, 345, 345, 234]

def test_5 ():
    assert mailroom.createdatadictionary('Dale') == {'Dale': [2050, 6, 341.67]}

