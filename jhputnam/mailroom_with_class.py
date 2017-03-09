#!/usr/bin/env python3


"""Mailroom script to send thank you emails to donors"""

import sys
import pickle
from mailroom_helper import *

DBFILE = "donordb.dat"


def print_help():
    """Function to print script usage."""

    print("Mailroom Usage:  <name>:add a donor and donation  h:help  l:list"
          "donors  r:print report q:quit")


def initdb(fname):
    """
    This function initializes the donor db using pickle.

    Args:
        fname: A file name for the pickle file.

    Returns:
        A dictionary object containing donors.

    Raises:
        FileNotFoundError: Is raised if opening the pickle file fails.
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
    Function to write the current donor dictionary out to a pickle file.

    Args:
        donors: Donor dictionary containing list of donors and the amounts.
        fname: File name for the pickle file.

    Raises:
        IOError: Raised when writing to the pickle file fails.
    """

    try:
        with open(fname, 'wb') as handle:
            pickle.dump(donors, handle, protocol=pickle.HIGHEST_PROTOCOL)
    except IOError:
        raise "Error writing to the donors file. Please check permissions."


def thank_donor(filename, donorname, donation):
    """
    Function generates a thank you text file if desired by the user.

    Args:
    filename: Name of the thank you file to write.
    donorname: Full name of donor.
    donation: The donation amount.

    Raises:
        IOError: Raised when unable to write the thank you file.
    """

    try:
        with open(filename, 'w') as fhandle:
            fhandle.write("Hello {}! On behalf of our staff here at OMGBBQMMX,"
                          "I want to thank you for your generous gift"
                          " of ${:.2f}!".format(donorname, donation))
            print("Email file generated!")

    except IOError:
        raise ("Unable to write thank you file. Please check"
               " permissions.")


def main():
    """
    Main entry point for the program.
    Collects user input and calls helper functions to process the data.

    Raises:
        ValueError: Raised when the user enters a dollar amount with other
        special characters or letters.
    """

    # Init donor dict from pickle file.
    donors = initdb(DBFILE)

    # Create an instance of the MailRoom class.
    mailroom = MailRoom(donors)

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
            mailroom.generate_report()
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
            continue

        # Add donation via the class and get back the updated dict.
        donors = mailroom.add_donation(donorname, donation)

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
