#!/usr/bin/env python3

#  http://uwpce-pythoncert.github.io/IntroToPython/exercises/mailroom.html
#  Lists now.  Tuples next.  Dictionaries later.


def load_donordb():
    """
    Instructions:
    1. It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each
    """

    donor_db = [
        "Aristotle", 384,
        "Aristotle", 322,
        "Kant", 1724,
        "Kant", 1804,
        "Locke", 1632,
        "Russell", 1872,
        "Russell", 1970,
        "Dennett", 1942,
        "Kant", 1785,
        "Russell", 1950,
    ]

    return donor_db


def get_donor_names(donor_db):
    names = []

    for i in range(len(donor_db)):
        if i % 2 == 0:  # if we have an even numebr we have a name
            names.append(donor_db[i])

    # Return a sorted, unique list of names
    return sorted(set(names))


def print_donor_names(donor_db):
    print(get_donor_names(donor_db))


def add_donation(db, donor, contribution):
    db.append(donor)  # Add the donor to the db
    db.append(int(contribution))  # Store as an int to facilitate mathematical operations


def tally_report(db):
    """
    Localize report calculations to this routine
    """

    donor_names = get_donor_names(db)
    donor_totals = [0] * len(donor_names)  # Create a list same length as donor_names initialized to zeros
    donor_num_gifts = [0] * len(donor_names)  # Create a list same length as donor_names initialized to zeros

    for i in range(len(db)):

        # if we have an even numebr we have a name
        if i % 2 == 0:
            # print("i is {0}, db[{0}] is {1}, db[{0}+1] is {2}".format(i, db[i], db[i + 1]))

            # Run through the donor list
            for j in range(len(donor_names)):
                # print("j is {0}, donor_names[{0}] is {1}".format(j, donor_names[j]))

                # If these match we have found a record for the current donor
                if db[i] == donor_names[j]:
                    # print("donor_totals[{0}] is {1}".format(j, donor_totals[j]))

                    # Tally up the donation, which is in the next index in the db/list
                    donor_totals[j] += db[i + 1]

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
    for i in range(len(names)):
        print("{0} | {1} | {2} | {3}".format(
            names[i].ljust(25),  # Left justify the names
            str(totals[i]).rjust(11),  # Need this as a string to facilitate justification
            str(num_gifts[i]).rjust(9),  # Need this as a string to facilitate justification
            totals[i] / num_gifts[i])
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
