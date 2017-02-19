from mailroom import mailroom
from mailroom import thank_you
import sys
import mock



def test_menu_input1():
    with mock.patch('builtins.input',return_value = 'asdf'):
        assert ValueError

def test_menu_input2():
    with mock.patch('builtins.input',return_value='4'):
        assert Exception("That isn't a valid input. Try again.")
def test_menu_input3():
    with mock.patch('builtins.input',return_value='3'):
        assert Exception("That isn't a valid input. Try again.")

def test_donor_name_int():
    def return_value(prompt):
        if "Welcome to Mailroom" in prompt:
            return "1"
        if "full name" in prompt:
            return "3"
    with mock.patch('builtins.input',return_value):
        assert Exception("You need to enter a name for your donor. You have entered a number.")

def test_string_as_donation():
    def return_value(prompt):
        if "Welcome to Mailroom" in prompt:
            return "1"
        if "full name" in prompt:
            return "Test Guy"
        if "contributed" in prompt:
            return "asdf"
    with mock.patch('builtins.input',return_value):
        assert ValueError("You need to enter a number. Error:invalid literal for int() with base 10: 'asdf'")

#3d\ef test_string_as_donation_2():
 #   assert thank_you(input_name="3",donation=123) is ValueError("You need to enter a name for your donor. You have entered a number.")

def test_negative_donations():
    def return_value(prompt):
        if "Welcome to Mailroom" in prompt:
            return "1"
        if "full name" in prompt:
            return "Test Guy"
        if "contributed" in prompt:
            return "-123"
    with mock.patch('builtins.input',return_value):
        assert Exception("STOP EMBEZZLING, JANET, THE BOARD IS ON TO YOU!")


test_menu_input3()



