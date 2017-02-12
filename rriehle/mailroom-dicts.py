#!/usr/bin/env python3

#  http://uwpce-pythoncert.github.io/IntroToPython/exercises/mailroom.html
#  Can we improve the code by pickling?

import pickle


def print_usage():
    print("mailroom>>  <name>:add a donor and donation  h:help  l:list donors  r:print report  t:thank donors  q:quit")


def load_donordb():
    try:
        with open('mailroom.pickle', 'rb') as db_handle:
            donor_db = pickle.load(db_handle)
    except IOError:
        donor_db = {
            "Aristotle": [384, 322],
            "Kant": [1724, 1804, 1785],
            "Locke": [1632],
            "Russell": [1872, 1970, 1950],
            "Dennett": [1942],
        }
    return donor_db


def save_donordb(db):
    try:
        with open('mailroom.pickle', 'wb') as db_handle:
            pickle.dump(db, db_handle)
    except IOError:
        raise "Error: Unable to save donor database."


def add_donation(db, donor, contribution):
    if donor in db.keys():
        db[donor].append(int(contribution))
    else:
        db[donor] = [int(contribution)]


def tally_report(values):
    donation_total = sum(values)
    num_gifts = len(values)
    average_gift = donation_total / num_gifts
    return str(donation_total), str(num_gifts), average_gift


def print_report(db):
    # Print a header
    print("Donor Name                | Total Given | Num Gifts | Average Gift")

    # Print each row
    for names, values in db.items():
        donation_total, num_gifts, average_gift = tally_report(values)

        print("{} | {} | {} | ${:11,.2f}".format(
            names.ljust(25),  # Left justify the names
            donation_total.rjust(11),
            num_gifts.rjust(9),
            average_gift,  # Handle formatting in the format string
        ))


def thank_donors(donor, amount):
    with open('mailroom-thankyou-{}.txt'.format(donor), 'w') as f:
        f.write("Thank you, {}, for your generous donation of ${}.\nSincerly, The Mailroom Team\n".format(donor, amount))


def list_donor_files():
    import glob
    print(glob.glob("mailroom-thankyou-*.txt"))


if __name__ == '__main__':
    print_usage()

    donor_db = load_donordb()

    while True:
        user_input = input("mailroom>>  ")

        # A handy way to break out of the loop/program
        if user_input == 'quit' or user_input == 'q':
            save_donordb(donor_db)
            break

        # If the user wants a help prompt, print it
        if user_input == 'help' or user_input == 'h':
            print_usage()
            continue

        # If the user wants a list of donors, print it and then continue with a new prompt
        if user_input == 'list' or user_input == 'l':
            print(sorted(set(donor_db.keys())))
            continue

        # If the user wants a report, print it and then continue with a new prompt
        if user_input == 'report' or user_input == 'r':
            print_report(donor_db)
            continue

        # Generate thank you letters and then continue
        if user_input == 'thanks' or user_input == 't':
            [thank_donors(name, sum(value)) for name, value in donor_db.items()]
            list_donor_files()
            continue

        # After the cases above we can assume that the input is a donor's name
        donor = user_input

        # We still need an amount
        contribution_amount = input("mailroom>>  How much is {} contributing? ".format(donor))

        # Add the donation to the db
        add_donation(donor_db, donor, contribution_amount)
