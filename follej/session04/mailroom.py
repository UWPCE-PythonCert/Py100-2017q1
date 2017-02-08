#!/usr/bin/env python3
import sys
from statistics import mean

donors = []
#
# donors[0] = ['William Gates, III', [65000, 68888.40]]
# donors[1] = ['Mark Zuckerberg', [65000, 68888.40, 600000]]
# donors[2] = ['Jeff Bezos',      [65000, 68888.40, 10000]]
# donors[3] = ['Paul Allen',      [65000, 68888.40]]
# donors[4] = ['Jesse Follet',    [0.65, 1.50]]
keys = ['First_Name', 'Last_Name', 'Donation_Amounts']
donors.append(dict(zip(keys, ["William", "Gates", [65000, 68888.40]])))
donors.append(dict(zip(keys, ["Jeff", "Bezos", [65000, 68888.40, 10000]])))
donors.append(dict(zip(keys, ["Mark", "Zuckerbert", [65000, 68888.40, 600000]])))
donors.append(dict(zip(keys, ["Paul", "Allen", [65000, 68888.40]])))
donors.append(dict(zip(keys, ["Jesse", "Follet", [0.65, 1.50]])))


def create_a_report():
    indices = sort_donors()
    print_a_report(indices)


def print_a_report(donor_index):
    header = 'Donor Name                | Total Given | Num Gifts | Average Gift'
    top_line = '-' * len(header)
    print(header)
    print(top_line)
    for i in donor_index:
        # print(donors[i][0].ljust(26), end='')
        print("{First_Name} {Last_Name}".format(**donors[i]).ljust(26), end='')
        print("$%12.2f" % (sum(donors[i]['Donation_Amounts'])), end='')
        print("%12d  " % (len(donors[i]['Donation_Amounts'])), end='')
        print("$%12.2f" % (mean(donors[i]['Donation_Amounts'])))
    print()


def sort_donors():
    amounts = []
    for i in range(len(donors)):
        amounts.append([sum(donors[i]['Donation_Amounts']), i])
    sort_amounts = sorted(amounts, reverse=True)
    sort_indices = []
    for i in range(len(sort_amounts)):
        sort_indices.append(sort_amounts[i][1])
    return sort_indices


def quit_app():
    print("Quitting!")
    sys.exit()


def init_menu():
    menu_items = {"Email a Thank you": send_a_thank_you, "Create a Report": create_a_report, "Quit": quit_app,
                  "Write letter to donors": write_letter_to_donor}
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


def write_letter_to_donor():
    for i in range(len(donors)):
        f = open('./Thank_you_to_{First_Name}_{Last_Name}.txt'.format(**donors[i]), 'w')
        lines = []
        lines.append("To {First_Name} {Last_Name}:\n".format(**donors[i]))
        lines.append("\n")
        lines.append("Thank you for you generous donation of $%.2f\n" % sum(donors[i]['Donation_Amounts']))
        lines.append("\n")
        lines.append("Sincerely,\n")
        lines.append("Gnrc Foundation\n")
        f.writelines(lines)
        f.close()
        print(f.name + " saved")
    print("")

def write_thank_you_email(donor_index):
    print("To {First_Name} {Last_Name}:".format(**donors[donor_index]))
    print()
    print("Thank you for you generous donation of $%.2f" % sum(donors[donor_index]['Donation_Amounts']))


def get_donor_names_list():
    donor_names = []
    for i in range(len(donors)):
        donor_names.append("{First_Name} {Last_Name}".format(**donors[i]))
    return donor_names


def send_a_thank_you():
    donor_names = get_donor_names_list()
    print("Hit 'Enter' at any prompt to return to main menu")
    response = input("Enter Name of donor or 'list' > ")
    if response == "list":
        for name in donor_names:
            print(name)
        print()
        send_a_thank_you()
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
        init_menu()


def add_donation(donor_index):
    response = input("Enter donation amount > ")
    if response == "":
        init_menu()
    donors[donor_index]['Donation_Amounts'].append(float(response))


def add_a_donor(new_donor):
    donor_name = new_donor.split()
    donors.append(dict(zip(keys, [donor_name[0], donor_name[1], []])))


if __name__ == '__main__':
    # send_a_thank_you()
    # write_thank_you_email(2)
    init_menu()
