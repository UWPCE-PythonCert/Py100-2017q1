from mailroom import mailroom
import sys
import mock



#def test_menu_input1():
    #assert "That isn't a valid input" in mailroom.main(response="4")

#def test_menu_input2():
    #with mock.patch('builtins.input',return_value='4'):
     #   assert Exception("That isn't a valid input. Try again.")
1
#def test_menu_input3():
    #with mock.patch('builtins.input',return_value='3'):
    #    assert Exception("That isn't a valid input. Try again.")

mr = mailroom()

def test_int_as_donor():
    assert mr.get_donor_name(input_name = "3", unit_test=True) is False

def test_str_as_donor():
    assert mr.get_donor_name(input_name= "New Donor", unit_test=True) is True

def test_int_as_donation():
    assert mr.get_donation(donation = "asdf", input_name = "New Donor", unit_test=True) is False
def test_negative_donation():
    assert mr.get_donation(donation = "-100", input_name = "Janets Vacation Fund", unit_test=True) is False
def test_good_donation():
    assert mr.get_donation(donation = "100", input_name = "New Donor", unit_test=True) is True
