#!/usr/bin/env python3

from mailroom import (
    sort_donors,
    is_valid_new_donor_name,
    get_donor_names_list,
    add_a_donor,
    donors
)


def test_sort_donors():
    assert sort_donors() == [2, 1, 3, 0, 4]


def test_is_valid_new_donor_name_is_true():
    assert is_valid_new_donor_name('Jesse Follet') is True


def test_is_valid_new_donor_name_is_false():
    assert is_valid_new_donor_name('Jesse') is False


def test_get_donor_names_list():
    assert get_donor_names_list() == ["William Gates", "Jeff Bezos", "Mark Zuckerbert", "Paul Allen", "Jesse Follet"]


def test_add_a_donor():
    new_donor_name = "Linus Torvald"
    add_a_donor(new_donor_name)
    assert donors[-1]['First_Name'] == 'Linus'
    assert donors[-1]['Last_Name'] == 'Torvald'
    assert donors[-1]['Donation_Amounts'] == []
