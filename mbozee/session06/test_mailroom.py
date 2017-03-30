#!/usr/bin/env python

import pytest
from mailroom import (
    add_donation,
)


def test_add_donation(new_donor, new_amount):
    new_donor = "mike"
    new_amount = -1

test_add_donation()