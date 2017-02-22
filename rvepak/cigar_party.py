#!/usr/bin/env python
"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of cigars.

Return True if the party with the given values is successful,
or False otherwise.
"""

limits = {'weekend': (40, None), 'weekday': (40, 60)}


def cigar_party(cigars, is_weekend):
    return_value = False
    if is_weekend:
        if cigars >= limits['weekend'][0]:
            return_value = True
    else:
        if cigars >= limits['weekday'][0] and cigars <= limits['weekday'][1]:
            print('In weekday')
            return_value = True
    return return_value
