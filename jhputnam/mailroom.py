#!/usr/bin/env python3

"""Mailroom script to send thank you emails to donors"""

DONORS = {"Derp McDerpston": [250.00, 650.00], "Billy Bob": [0.02],
          "Cthulhu": [1000.00, 25000.0, 123456.0],
          "Kayaba Akihiko": [10000.00, 3853.00, 6147.00],
          "Doctor Evil": [1000000.00]}


def menu():
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
        send_thank_you()
    elif choice == 2:
        generate_report()
    else:
        print("Goodbye!")


def send_thank_you():
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
            for name in DONORS:
                print(name)
                continue
        else:
            break

    # Don't like this much. Would be nice to make this better.
    if fullname not in DONORS:
        print("The name \'{}\' is not in the donor list. Auto adding the "
              "name as a new donor.\n".format(fullname))
        donation = add_donor(fullname)
    else:
        print("The name \'{}\' was found in the donor list. Adding new "
              "donation.\n".format(fullname))
        donation = add_donor(fullname)

    print()
    print("Dear {},\n".format(fullname))
    print()
    print("On behalf of our staff here at OMGBBQMMX, I want to thank you for "
          "your generous gift of ${:.2f}!!!11oneone".format(donation))
    print()
    input("Press Enter key to continue")

    menu()


def add_donor(fullname):
    """
    Function to add a donor and donation amount to the dataset.
    Arguments:
    fullname -- Full donor name.
    returns -- donation amount.
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

    if fullname not in DONORS:
        DONORS[fullname] = [donation]
    else:
        DONORS[fullname].append(donation)

    return donation


def generate_report():
    """
    Function to genereate a report sorted by donation amount.
    """


def main():
    """
    Main entry point to the script.
    Displays initial menu and calls various functions depending on user input.
    """

    # Show menu.
    menu()

if __name__ == '__main__':
    main()
