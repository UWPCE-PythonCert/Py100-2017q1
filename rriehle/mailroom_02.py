#!/usr/bin/env python3

#  http://uwpce-pythoncert.github.io/IntroToPython/exercises/mailroom.html
#  Can we improve the code by introducing tuples?

NAME = 0  # Donor names show up in position 0 of the db tuple
AMOUNT = 1  # Donation amounts show up in position 1 of the db tuple


def initialize_donordb():
    """
    Instructions:
    1. It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each
    """

    # Use tuples rather than a flat list to pin down the 'db'
    donor_db = [
        ("Aristotle", 384),
        ("Aristotle", 322),
        ("Kant", 1724),
        ("Kant", 1804),
        ("Locke", 1632),
        ("Russell", 1872),
        ("Russell", 1970),
        ("Dennett", 1942),
        ("Kant", 1785),
        ("Russell", 1950),
    ]

    return donor_db


def get_donor_names(donor_db):
    names = []

    for i in range(len(donor_db)):
        names.append(donor_db[i][NAME])

    # Return a sorted, unique list of names
    return sorted(set(names))


def print_donor_names(donor_db):
    print(get_donor_names(donor_db))


def add_donation(db, donor, contribution):
    db.append((donor, int(contribution)))


def tally_report(db):
    """
    Localize report calculations to this routine
    """

    donor_names = get_donor_names(db)
    donor_totals = [0] * len(donor_names)  # Create a list same length as donor_names initialized to zeros
    donor_num_gifts = [0] * len(donor_names)  # Create a list same length as donor_names initialized to zeros

    for i in range(len(db)):
        # print("i is {0}, db[{0}][NAME] is {1}, db[{0}][AMOUNT] is {2}".format(i, db[i][NAME], db[i][AMOUNT]))  # debug

        # Run through the donor list
        for j in range(len(donor_names)):
            # print("j is {0}, donor_names[{0}] is {1}".format(j, donor_names[j]))  # debug

            # # If these match we have found a record for the current donor
            if db[i][NAME] == donor_names[j]:

                # Tally up the donation
                donor_totals[j] += db[i][AMOUNT]

                # Increment the number of gifts associated with this donor
                donor_num_gifts[j] += 1

    # print(donor_totals)  # debug
    # print(donor_num_gifts)  # debug

    return donor_names, donor_totals, donor_num_gifts


def print_report(names, totals, num_gifts):
    """
    Localize report i/o to this routine
    """

    # Print a header
    print("Donor Name                | Total Given | Num Gifts | Average Gift")

    # Print each row
    for name, total, num in zip(names, totals, num_gifts):
        print("{0} | {1} | {2} | {3}".format(
            name.ljust(25),  # Left justify the names
            str(total).rjust(11),  # Need this as a string to facilitate justification
            str(num).rjust(9),  # Need this as a string to facilitate justification
            total / num)
        )


def thank_donor(donor, amount):
    print("Thank you, {}, for your generous donation of ${}.".format(donor, amount))


if __name__ == '__main__':
    """
    Instructions
    2. The script should prompt the user (you) to choose from a menu of 3 actions: ‘Send a Thank You’ or ‘Create a Report’ or ‘quit’)
    """
    donor_db = initialize_donordb()

    while True:
        user_input = input("<name> add a donor and donation  l: list donors  r: print a report  q: quit >> ")

        # A handy way to break out of the loop/program
        if user_input == 'quit' or user_input == 'q':
            break

        # If the user wants a list of donors, print it and then continue with a new prompt
        if user_input == 'list' or user_input == 'l':
            print_donor_names(donor_db)
            continue

        # If the user wants a report, print it and then continue with a new prompt
        if user_input == 'report' or user_input == 'r':
            names, totals, num_gifts = tally_report(donor_db)
            print_report(names, totals, num_gifts)
            continue

        # After the cases above we can assume that the input is a donor's name
        donor = user_input

        # We still need an amount
        contribution_amount = input("How much is {} contributing? >> ".format(donor))

        # Add the donation to the db
        add_donation(donor_db, donor, contribution_amount)

        # Thank the donor
        thank_donor(donor, contribution_amount)
