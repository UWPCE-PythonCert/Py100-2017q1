#!/usr/bin/env python3


"""Mailroom script to send thank you emails to donors"""

import sys
from operator import itemgetter
import pickle

DBFILE = "donordb.dat"


def print_help():
    """Function to print script usage."""

    print("Mailroom Usage:  <name>:add a donor and donation  h:help  l:list"
          "donors  r:print report  t:thank donors  q:quit")


def initdb(fname):
    """
    This function initializes the donor db using pickle.
    returns donor dictionary.
    """

    try:
        with open(fname, 'rb') as handle:
            donors = pickle.load(handle)

    except FileNotFoundError:
        print("Database file 'donordb.dat' not found!"
              " What would you like to do?\n 1. Create new database.\n"
              " 2. Abort\n\n")

        while True:
            choice = input("Enter option 1 or 2: ")
            if choice not in ('1', '2'):
                print("Not a valid option. Try again.")
                continue
            break

        if choice == '1':
            donors = {}
            updatedb(donors, fname)

        elif choice == '2':
            print("Goodbye!")
            sys.exit()

    return donors


def updatedb(donors, fname):
    """
    Function to write the donor dictionary out to a pickle file.
    """

    try:
        with open(fname, 'wb') as handle:
            pickle.dump(donors, handle, protocol=pickle.HIGHEST_PROTOCOL)
    except IOError:
        raise "Error writing to the donors file. Please check permissions."


def add_donation(donors, donorname, donation):
    """
    Function to handle adding donations.
    Arguments:
    donors: donors dictionary object.
    """

    if donorname not in donors:
        print("The name \'{}\' is not in the donor database. Adding name"
              " as a new donor.\n".format(donorname))
        donors[donorname] = [donation]
    else:
        print("The name \'{}\' was found in the donor database. Adding new"
              " donation.\n".format(donorname))
        donors[donorname].append(donation)

    return donors


def thank_donor(filename, donorname, donation):
    """
    Function generates a thank you text file if desired by the user.
    Arguments:
    fullname: Full name of donor.
    donation: The donation amount.
    """

    try:
        with open(filename, 'w') as fhandle:
            fhandle.write("Hello {}! On behalf of our staff here at OMGBBQMMX,"
                          "I want to thank you for your generous gift"
                          "of ${:.2f}!".format(donorname, donation))
            print("Email file generated!")

    except IOError:
        raise ("Unable to write thank you file. Please check"
               " permissions.")


def sum_report(values):
    """
    Function to tally donations for report generation.
    """

    donation_total = sum(values)
    num_gifts = len(values)
    average_gift = donation_total / num_gifts

    return donation_total, num_gifts, average_gift


def generate_report(donors):
    """
    Function to genereate a report sorted by donation amount.
    """

    print()
    print("     NAME            TOTAL          NUMBER       AVERAGE ")
    print("----------------------------------------------------------")

    for name, value in sorted(donors.items(), key=itemgetter(1),
                              reverse=True):

        donation_total, donations, average_donations = sum_report(value)
        print("{:<20} ${:<15.2f} {:<8} ${:<0.2f}".format(name, donation_total,
                                                         donations,
                                                         average_donations))


def main():
    """
    Main entry point for the program.
    Collects user input and calls functions with that input.
    """

    # Init donor dict from pickle file.
    donors = initdb(DBFILE)
    # Print usage when the program starts.
    print_help()

    while True:

        # Get uer input and try to validate that it is a name or command.
        user_input = input("Mailroom command>> ")

        # Check for people whacking enter a bunch of times, like me.
        if user_input == "":
            continue

        if user_input.isdigit():
            print("Please input a command or name only. No numbers.")
            continue

        # Break out if quit.
        if user_input == 'quit' or user_input == 'q':
            updatedb(donors, DBFILE)
            break

        # Print help if requested.
        if user_input == 'help' or user_input == 'h':
            print_help()
            continue

        # List donor names if requested.
        if user_input == 'list' or user_input == 'l':
            _ = {print(k) for k in donors}
            continue

        # Generate donor report if requested.
        if user_input == 'report' or user_input == 'r':
            generate_report(donors)
            continue

        # Safe to assume the input was a name?
        donorname = user_input
        try:
            donation = float(input("How much is {} contributing? "
                                   .format(donorname)))
            if donation <= 0:
                print("Enter donation amount greater than zero please.\n")
                continue
        except ValueError:
            print("Bad value! Please enter numbers only.")

        # Add donation to the dict.
        add_donation(donors, donorname, donation)

        while True:
            send_ty = input("Would you like to generate a thank you email?"
                            " y/n: ").lower()
            if send_ty not in ('y', 'yes', 'n', 'no'):
                print("Please answer y or n (yes or no also acceptable).\n")
                continue

            if send_ty == 'yes' or send_ty == 'y':
                thank_donor('email-file-{}'.format(donorname), donorname,
                            donation)
                break
            else:
                break


if __name__ == '__main__':
    sys.exit(main())
