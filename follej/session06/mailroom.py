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


def safe_input(prompt):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None


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
    """
    Sort the donors list by total overall donation from most to least.
    Returns an array index
    """
    amounts = [(sum(donor['Donation_Amounts']), i) for i, donor in enumerate(donors)]
    sort_indices = [value[1] for value in sorted(amounts, reverse=True)]
    return sort_indices


def quit_app():
    print("Quitting!")
    sys.exit()


def init_menu():
    menu_items = {"Email a Thank you": send_a_thank_you, "Create a Report": create_a_report, "Quit": quit_app,
                  "Write letter to donors": write_letter_to_donor}
    while True:
        print("Enter string from items below:")
        [print("{}".format(item)) for item in sorted(menu_items)]
        response = safe_input("> ")
        if response is None:
            quit_app()
        print(response)
        if response in menu_items:
            menu_items[response]()
        else:
            print("Invalid entry.  Try again.")
            print("")


def write_letter_to_donor():
    for i in range(len(donors)):
        f = open('./Thank_you_to_{First_Name}_{Last_Name}.txt'.format(**donors[i]), 'w')
        lines = ["To {First_Name} {Last_Name}:\n".format(**donors[i]), "\n",
                 "Thank you for you generous donation of $%.2f\n" % sum(donors[i]['Donation_Amounts']), "\n",
                 "Sincerely,\n", "Gnrc Foundation\n"]
        f.writelines(lines)
        f.close()
        print(f.name + " saved")
    print("")


def write_thank_you_email(donor_index):
    print("To {First_Name} {Last_Name}:".format(**donors[donor_index]))
    print()
    print("Thank you for you generous donation of $%.2f" % sum(donors[donor_index]['Donation_Amounts']))


def get_donor_names_list():
    # Changed to comprehension
    donor_names = ["{First_Name} {Last_Name}".format(**donors[i]) for i in range(len(donors))]
    return donor_names


def is_valid_new_donor_name(new_donor):
    donor_name = new_donor.split()
    if len(donor_name) != 2:
        print("Invalid input:  Must type a first name and last name!")
        print()
        return False
    return True


def send_a_thank_you():
    donor_names = get_donor_names_list()
    print("Hit 'Enter' at any prompt to return to main menu")
    response = safe_input("Enter Name of donor or 'list' > ")
    if response is None:
        quit_app()
    if response == "list":
        print("\n".join(donor_names))
        print()
        send_a_thank_you()
    elif response in donor_names:
        donor_index = donor_names.index(response)
        add_donation(donor_index)
        print_a_report([donor_index])
        write_thank_you_email(donor_index)
    elif response != "":
        if not is_valid_new_donor_name(response):
            send_a_thank_you()
        add_a_donor(response)
        donor_names = get_donor_names_list()
        print(donor_names)
        donor_index = donor_names.index(response)
        add_donation(donor_index)
        print_a_report([donor_index])
        write_thank_you_email(donor_index)
    else:
        init_menu()


def add_a_donor(new_donor):
    donor_name = new_donor.split()
    # Requires a first and a last - for now. Add some kind of exception?
    donors.append(dict(zip(keys, [donor_name[0], donor_name[1], []])))


def add_donation(donor_index):
    while True:
        response = safe_input("Enter donation amount > ")
        if response is None:  # escape code entered
            quit_app()
        elif response == "":
            init_menu()
        elif not response.isnumeric():
            print("Invalid Input")
        else:
            donors[donor_index]['Donation_Amounts'].append(float(response))
            break


if __name__ == '__main__':
    init_menu()
