# Javier Vazquez
# Grid Printer
# Feb 20, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/functions_as_args.html

import os

def hand_weapon():
    return 0

def gun():
    return 0

def flower_power():
    pass

def score(weapon_type, weapon_size):
    if weapon_type == hand_weapon and weapon_size == "small":
        return hand_weapon() + 1
    elif weapon_type == hand_weapon and weapon_size == "medium":
        return hand_weapon() + 2
    elif weapon_type == hand_weapon and weapon_size == "large":
        return hand_weapon() + 3
    elif weapon_type == gun and weapon_size == "small":
        return gun() + 5

def test_scoring():
    assert score(hand_weapon, 'small') == 1
    assert score(hand_weapon, 'medium') == 2
    assert score(hand_weapon, 'large') == 3
    assert score(gun, 'small') == 5
    # assert score(gun, 'medium') == 8
    # assert score(gun, 'large') == 13
    # assert score(flower_power, 'small') == 21
    # assert score(flower_power, 'medium') == 34
    # assert score(flower_power, 'large') == 55


# if __name__ == '__main__':
#     print(os.path.basename(__file__))
#     main()