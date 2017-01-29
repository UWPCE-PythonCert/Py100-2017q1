#!/usr/bin/env python3

donors = {
    'Donovan Leitch': [100, 20, 150],
    'Stevie Nicks': [200, 80],
    'Ian Anderson': [190],
    'Mavis Staples': [170, 40, 130],
    'Suzanne Vega': [160, 30]
}


def thank_you():
    """Write a thank you letter."""
    print('test')


def menu():
    """Give user choice of actions."""
    options = {1: 'Send a Thank You', 2: 'Create a Report', 3: 'quit'}
    choice = input("Choose an option:\n" + str(options) + " > ")
    if choice == str(1):
        thank_you()

menu()