#!/usr/bin/env python3
import sys
from statistics import mean

donors = [[]] * 5

donors[0] = ['William Gates, III', [65000, 68888.40]]
donors[1] = ['Mark Zuckerberg', [65000, 68888.40, 600000]]
donors[2] = ['Jeff Bezos', [65000, 68888.40, 10000]]
donors[3] = ['Paul Allen', [65000, 68888.40]]
donors[4] = ['Jesse Follet', [0.65, 1.50]]


# TODO - make the above a dictionary?

def create_a_report():
    indices = sort_donors()
    print_a_report(indices)


def print_a_report(indices):
    header = 'Donor Name                | Total Given | Num Gifts | Average Gift'
    top_line = '-' * len(header)
    print(header)
    print(top_line)
    for i in indices:
        print(donors[i][0].ljust(26), end='')
        print("$%12.2f" % (sum(donors[i][1])), end='')
        print("%12d  " % (len(donors[i][1])), end='')
        print("$%12.2f" % (mean(donors[i][1])))
    print()


def sort_donors():
    amounts = []
    for i in range(len(donors)):
        amounts.append([sum(donors[i][1]), i])
    sort_amounts = sorted(amounts, reverse=True)
    sort_indices = []
    for i in range(len(sort_amounts)):
        sort_indices.append(sort_amounts[i][1])
    return sort_indices


def quit_app():
    print("Quitting!")
    sys.exit()


def init_menu():
    menu_items = {"Email a Thank you": send_a_thank_you, "Create a Report": create_a_report, "Quit": quit_app}
    while 1:
        print("Enter string from items below:")
        for item in sorted(menu_items):
            print("{}".format(item))
        response = input("> ")
        print(response)
        if response in menu_items:
            menu_items[response]()
        else:
            print("Invalid entry.  Try again.")
            print("")


def write_thank_you_email(donor_index):
    print("To {}:".format(donors[donor_index][0]))
    print()
    print("Thank you for you generous donation of $%.2f" % sum(donors[donor_index][1]))


def get_donor_names_list():
    donor_names = []
    for i in range(len(donors)):
        donor_names.append(donors[i][0])
    return donor_names


def send_a_thank_you():
    donor_names = get_donor_names_list()
    print("Hit 'Enter' at any prompt to return to main menu")
    response = input("Enter Name of donor or 'list' > ")
    if response == "list":
        for name in donor_names:
            print(name)
        print()
    elif response in donor_names:
        donor_index = donor_names.index(response)
        add_donation(donor_index)
        print_a_report([donor_index])
        write_thank_you_email(donor_index)
    elif response != "":
        add_a_donor(response)
        donor_names = get_donor_names_list()
        donor_index = donor_names.index(response)
        add_donation(donor_index)
        print_a_report([donor_index])
        write_thank_you_email(donor_index)
    else:
        send_a_thank_you()


def add_donation(donor_index):
    response = input("Enter donation amount > ")
    if response == "": init_menu()
    donors[donor_index][1].append(float(response))


def add_a_donor(new_donor):
    donors.append([new_donor, []])


if __name__ == '__main__':
    # send_a_thank_you()
    # write_thank_you_email(2)
    init_menu()
