from mailroom import mailroom
import sys
import mock



def test_menu_input1():
    assert "That isn't a valid input" in mailroom.main(response="4")

def test_menu_input2():
    with mock.patch('builtins.input',return_value='4'):
        assert Exception("That isn't a valid input. Try again.")

def test_menu_input3():
    with mock.patch('builtins.input',return_value='3'):
        assert Exception("That isn't a valid input. Try again.")



