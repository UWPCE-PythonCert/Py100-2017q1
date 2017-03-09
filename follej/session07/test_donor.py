#!/usr/bin/env python3

import pytest

from donor import Donor


@pytest.fixture(scope='module')
def test_donor():
    donor = Donor("Jesse", "Follet")
    donor.add_donation(1000)
    donor.add_donation(500)
    return donor


def test_add_donation(test_donor):
    test_donor.add_donation(1500)
    assert test_donor.donations[-1] == 1500


def test_donation_stats(test_donor):
    assert test_donor.sum_donation() == 3000
    assert test_donor.number_of_donations() == 3
    assert test_donor.mean_donation() == 1000


@pytest.fixture(scope='module')
def test_donors():
    donors = [Donor("Jesse", "Follet")]
    donors[0].add_donation(1000)
    donors[0].add_donation(500)
    donors.append(Donor("Jesse", "Follet2"))
    donors[1].add_donation(500)
    return donors


def test_donors_sort(test_donors):
    # for i, donor in enumerate(test_donors):
    #     print(donor.print_donor_contributions())
    assert (sorted(test_donors, reverse=False) == [test_donors[1], test_donors[0]])
