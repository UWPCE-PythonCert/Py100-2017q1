#!/usr/bin/env python3

"""Dict and set lab."""


def delete_cake(dic):
    """Delete delicious cake."""

    dic.pop("cake")
    print(dic)


def add_mango(dic):
    """Add a mango."""

    dic.update({"fruit": "Mango"})
    print(dic)


def display_keys(dic):
    """Display keys."""

    for key in dic:
        print(key)


def display_values(dic):
    """Display values."""

    for key in dic:
        print(dic[key])


def is_the_cake_a_lie(dic):
    """Check dic for cake."""

    print("cake" in dic)


def is_mango(dic):
    """Check dic for mango."""

    print("Mango" in dic.values())


def new_with_tcount(dic):
    """
    Make a new dict with same keys but with the number of T's as the value.
    """

    # Put the cake back in the dic.
    dic.update({"cake": "Chocolate"})

    newdic = {}
    for key, val in dic.items():
        if "t" in val.lower():
            newdic.update({key: val.lower().count("t")})

    print(newdic)


def set3_subset_set2(set3, set2):
    """Check if set3 is a subset of set2."""

    print(set3.issubset(set2))


def set4_subset_set2(set4, set2):
    """Check if set4 is a  subset of set2."""

    print(set4.issubset(set2))


def create_and_add():
    """Create a new set and add the letter i to it."""

    newset = set("Python")
    newset.add("i")
    print(newset)

    return newset


def create_frozenset(newset):
    """Create frozenset and display union and intersection."""

    frozen = frozenset("marathon")
    print(newset.union(frozen))
    print(newset.intersection(frozen))


def build_sets():
    """
    Build sets.
    Returns set2, set3, and set4.
    """

    set2 = set()
    set3 = set()
    set4 = set()
    for i in range(1, 20):
        if i % 2 == 0:
            set2.add(i)
        if i % 3 == 0:
            set3.add(i)
        if i % 4 == 0:
            set4.add(i)

    return set2, set3, set4


def main():
    """Main function"""

    dic = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

    # Display the orig dict.
    print(dic)

    # Delete cake.
    delete_cake(dic)

    # Add mango.
    add_mango(dic)

    # Display keys.
    display_keys(dic)

    # Display values.
    display_values(dic)

    # Is cake in dic?
    is_the_cake_a_lie(dic)

    # Is mango in there?
    is_mango(dic)

    # New dic with t count.
    new_with_tcount(dic)

    # Create and display sets.
    set2, set3, set4 = build_sets()
    print(set2)
    print(set3)
    print(set4)

    # Is set3 a subset of set2?
    set3_subset_set2(set3, set2)

    # Is set4 a subset of set2?
    set4_subset_set2(set4, set2)

    # Create new set out of Python and add i.
    newset = create_and_add()

    # Create a frozenset and display union and intersection.
    create_frozenset(newset)


if __name__ == '__main__':
    main()
