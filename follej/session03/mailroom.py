#!/usr/bin/env python3
from statistics import mean

donors = [[]] * 5

donors[0] = ['William Gates, III', [65000, 68888.40]]
donors[1] = ['Mark Zuckerberg', [65000, 68888.40, 600000]]
donors[2] = ['Jeff Bezos', [65000, 68888.40, 10000]]
donors[3] = ['Paul Allen', [65000, 68888.40]]
donors[4] = ['Jesse Follet', [0.65, 1.50]]


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
    quit()


def init_menu():
    response = 0
    while response != 3:
        print("1) Sent a Thank You")
        print("2) Create a Report")
        print("3) Quit")
        response = int(input("> "))
        print(response)
        if response == 1:
            send_a_thank_you()
        elif response == 2:
            create_a_report()
        else:
            pass


def write_thank_you_email(param):
    pass


def send_a_thank_you():
    donor_names = []
    for i in range(len(donors)):
        donor_names.append(donors[i][0])

    response = "list"
    while response != "":
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
            write_thank_you_email([donor_names.index(response)])
        elif response != "":
            add_a_donor(response)
            donor_index = donors.index(response)
            add_donation(donor_index)
        else:
            pass


def add_donation(donor_index):
    response = input("Enter donation amount > ")
    if response == "": init_menu()
    donors[donor_index][1].append(int(response))


def add_a_donor(new_donor):
    donors.append([new_donor])


if __name__ == '__main__':
    send_a_thank_you()
    # init_menu()
