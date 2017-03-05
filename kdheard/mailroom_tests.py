import mailroom


def test_menu_input1(capsys):
    mailroom.main(response=4)
    exp_out = "That isn't a valid input. Try again.\n"
    out, err = capsys.readouterr()
    assert out == exp_out


def test_menu_input2(capsys):
    mailroom.main(response='asdf')
    exp_out = "\nThat isn't a valid input. Try again. \nError:invalid literal for int() with base 10: 'asdf'\n"
    out, err = capsys.readouterr()
    assert out == exp_out


def test_int_as_donor(capsys):

    mailroom.get_donor_name(input_name = "3")
    exp_out = 'You need to enter a name for your donor. You have entered a number.\n'
    out, err = capsys.readouterr()
    assert out == exp_out

def test_str_as_donor(capsys):
    inp = mailroom.get_donor_name(input_name= "New Donor", unit_test=True)
    out, err = capsys.readouterr()
    assert out == ""
    assert inp == True

