#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of cigars.

Return True if the party with the given values is successful,
or False otherwise.
"""


def cigar_party(cigars, is_weekend):
    # # Test 1
    # if cigars == 30 and not is_weekend:
    #     return False
    # # Test 2
    # elif cigars == 50 and not is_weekend:
    #     return True
    # # Test 3
    # elif cigars == 70 and is_weekend:
    #     return True
    # # Test 4
    # elif cigars == 30 and is_weekend:
    #     return False
    # # Test 5
    # elif cigars == 50 and is_weekend:
    #     return True
    # # Test 6
    # elif cigars == 60 and not is_weekend:
    #     return True
    # # Test 7
    # elif cigars == 61 and not is_weekend:
    #     return False
    # # Test 8
    # elif cigars == 40 and not is_weekend:
    #     return True
    # # Test 9
    # elif cigars == 39 and not is_weekend:
    #     return False
    # # Test 10
    # elif cigars == 40 and is_weekend:
    #     return True
    # # Test 11
    # elif cigars == 39 and is_weekend:
    #     return False

    # if 40 <= cigars <= 60 and is_weekend:
    #     return True
    # elif cigars >= 40 and not is_weekend:
    #     return True
    # else:
    #     return False

    if is_weekend and 40 <= cigars:
        return True
    elif not is_weekend and 40 <= cigars <= 60:
        return True
    else:
        return False