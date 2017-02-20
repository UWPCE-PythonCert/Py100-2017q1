"""
Mailroom testing.
"""

import pickle
import pytest

import mailroom


def test_initdb_dbpresent():
    """Test dbinit with db file present."""

    testdb = {'Dan Rather': [3453.0], 'SpongeBob': [44.05]}

    # Call initdb with test data.
    donors = mailroom.initdb('testdb.dat')

    # Assert that the test data is what we expect.
    assert donors == testdb


def test_initdb_dbmissing1(monkeypatch):
    """Test dninit function with db missing and option 1."""

    # Override input and supply option 1.
    monkeypatch.setitem(__builtins__, 'input', lambda x: '1')

    # Call initdb to assign donors.
    donors = mailroom.initdb('testdb2.dat')

    # Assert that the dict is empty.
    assert donors == {}


def test_initdb_dbmissing2(monkeypatch, capsys):
    """Test dbinit function with db missing and option 2."""

    # Override input and supply option 2.
    monkeypatch.setitem(__builtins__, 'input', lambda x: '2')

    # Catch the SystemExit.
    with pytest.raises(SystemExit):
        mailroom.initdb('testdb3.dat')

    # Grab the output, and ignore the err.
    out, _ = capsys.readouterr()

    # Assert that the output is what we expected.
    assert out == ("Database file 'donordb.dat' not found!"
                   " What would you like to do?\n 1. Create new database.\n"
                   " 2. Abort\n\n\nGoodbye!\n")


def test_updatedb():
    """Test updatedb function."""

    updatedb = {'Dan Rather': [3453.0], 'SpongeBob': [44.05],
                "Howard Dean": [25.55]}

    fname = 'updatedb.dat'
    # Call function with updated db and filename.
    mailroom.updatedb(updatedb, fname)
    # Open resulting pickle file.
    with open(fname, 'rb') as handle:
        data = pickle.load(handle)
    # Assert that data is as expected.
    assert data == updatedb


def test_add_donation():
    """Test add_donaton function with an existing name and a new name."""

    orig_dict = {"Kazuto Kirigaya": [16.00], "Uncle Mugen": [1000000]}

    added_to_kazuto = {"Kazuto Kirigaya": [16.00, 2022.00],
                       "Uncle Mugen": [1000000]}

    added_moot = {"Kazuto Kirigaya": [16.00, 2022.00],
                  "Uncle Mugen": [1000000], "moot": [1.00]}

    # Call add_donation with an existing name to add a donation.
    data = mailroom.add_donation(orig_dict, "Kazuto Kirigaya", 2022.00)

    # Assert that the data is what we expect.
    assert data == added_to_kazuto

    # Call add_donation again, only this time with a new name.
    data = mailroom.add_donation(orig_dict, "moot", 1.00)

    # Again check if the data is what we expect.
    assert data == added_moot


def test_thank_donor(tmpdir):
    """Test thank_donor function."""

    expected = ("Hello Test User! On behalf of our staff here at OMGBBQMMX,I"
                " want to thank you for your generous giftof $22.00!")

    # Set temp file name.
    filepath = tmpdir.join('test-email.txt')

    # Call thank user function with the appropriate data.
    mailroom.thank_donor(str(filepath), "Test User", 22.00)

    assert filepath.read() == expected


def test_sum_report():
    """Test sum_report function."""

    test_values = [2000.00, 2000.00, 400.00, 44.44]

    total, num, average = mailroom.sum_report(test_values)

    assert total == 4444.44
    assert num == 4
    assert average == 1111.11


def test_generate_report(capsys):
    """Test generate report function."""

    test_data = {"Kazuto Kirigaya": [16.00, 2022.00, 2026.00],
                 "Uncle Mugen": [1000000.00], "moot": [1.00, 2.00, 3.00]}

    # Call generate_report with the test data above.
    mailroom.generate_report(test_data)

    # Grab stdout, ignoring stderr in this case.
    out, _ = capsys.readouterr()

    # Test that out is what we expect.
    assert out == ("\n     NAME            TOTAL          NUMBER       AVERAGE"
                   " \n-------------------------------------------------------"
                   "---\nUncle Mugen          $1000000.00      1        "
                   "$1000000.00\nKazuto Kirigaya      $4064.00         3      "
                   "  $1354.67\nmoot                 $6.00            3       "
                   " $2.00\n")
