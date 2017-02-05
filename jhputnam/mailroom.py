#!/usr/bin/env python3

"""Mailroom script to send thank you emails to donors"""

import sys
from operator import itemgetter
import pickle


def initdb():
    """
    This function initializes the donor db using pickle.
    returns donor dictionary.
    """

    try:
        with open('donordb.dat', 'rb') as handle:
            donors = pickle.load(handle)

    except FileNotFoundError:
        print("Database file 'donordb.dat' not found! "
              "What would you like to do?\n")
        print("1. Create new database.")
        print("2. Abort.\n")
        print()

        while True:
            try:
                choice = int(input("Enter option 1 or 2: "))
                if choice not in (1, 2):
                    print("Not a valid option. Try again.")
                    continue
                break
            except ValueError:
                print("Not a valid option. Try again.")

        if choice == 1:
            donors = {}
            updatedb(donors)

        elif choice == 2:
            print("Goodbye!")
            sys.exit()

    return donors


def updatedb(donors):
    """
    Function to write the donor dictionary out to a pickle file.
    """

    with open('donordb.dat', 'wb') as handle:
        pickle.dump(donors, handle, protocol=pickle.HIGHEST_PROTOCOL)


def menu(donors):
    """
    Function to show the main menu.
    """

    # Originally put the menu in main() but ran into a roadblock when
    # the lab asked to return to the menu. Not sure how to do that in main
    # without getting into trouble.

    print("Welcome to mailroom. Please pick one of the following options:\n")
    print("1. Send a thank you")
    print("2. Generate report")
    print("3. Quit\n")

    while True:
        try:
            choice = int(input("Enter 1, 2, or 3 from the menu above: "))
            if choice not in (1, 2, 3):
                print("Not a valid option. Try again.")
                continue
            break
        except ValueError:
            print("Not a valid option. Try again.")

    if choice == 1:
        send_thank_you(donors)
    elif choice == 2:
        generate_report(donors)
    else:
        print("Goodbye!")


def send_thank_you(donors):
    """
    Function to handle both adding new users and to initiate the sending
    of a thank you email to the donor.
    """

    while True:
        fullname = input("Please enter the donor's full name or type 'list' "
                         "to see a list of donors: ")

        # Listing is not currnetly pretty.
        # Might clean up the presentation if time allows.
        if fullname == "list":
            for name in donors:
                print(name)
                continue
        else:
            break

    # Don't like this much. Would be nice to make this better.
    if fullname not in donors:
        print("The name \'{}\' is not in the donor list. Auto adding the "
              "name as a new donor.\n".format(fullname))
        donation = add_donor(donors, fullname)
    else:
        print("The name \'{}\' was found in the donor list. Adding new "
              "donation.\n".format(fullname))
        donation = add_donor(donors, fullname)

    print()
    print("Dear {},\n".format(fullname))
    print()
    print("On behalf of our staff here at OMGBBQMMX, I want to thank you for "
          "your generous gift of ${:.2f}!".format(donation))
    print()
    input("Press Enter key to continue")

    menu(donors)


def add_donor(donors, fullname):
    """
    Function to add a donor and donation amount to the dataset.
    Arguments:
    fullname -- Full donor name.
    returns donation amount.
    """

    while True:
        try:
            donation = float(input("Enter a donation amount for \'{}\': "
                                   .format(fullname)))
            break
        except ValueError:
            print("Bad value! Please enter a dollar amount without the "
                  "dollar sign.")
            continue

    if fullname not in donors:
        donors[fullname] = [donation]
    else:
        donors[fullname].append(donation)

    updatedb(donors)

    return donation


def generate_report(donors):
    """
    Function to genereate a report sorted by donation amount.
    """

    # Total up donations for each donor, and add to a new dict.
    total_donor_list = dict(zip(donors.keys(), [[sum(amount)] for amount in
                                                donors.values()]))

    for name in donors:
        # Get number of donations and add it to the new dict.
        num_of_donations = len(donors[name])
        total_donor_list[name].append(num_of_donations)

        # Calculate average donation, and add that too.
        donation_average = total_donor_list[name][0] / num_of_donations
        total_donor_list[name].append(donation_average)

    print()
    print("     NAME            TOTAL          NUMBER       AVERAGE ")
    print("----------------------------------------------------------")

    for name, value in sorted(total_donor_list.items(), key=itemgetter(1),
                              reverse=True):
        print("{:<20} ${:<15.2f} {:<8} ${:<0.2f}".format(name, value[0],
                                                         value[1], value[2]))
    print()
    input("Press Enter to continue")
    menu(donors)


def main():
    """
    Main entry point to the script.
    Displays initial menu and calls various functions depending on user input.
    """

    # Init the donor databse and get the donor dictionary.
    donors = initdb()
    # Show menu.
    menu(donors)


if __name__ == '__main__':
    main()
