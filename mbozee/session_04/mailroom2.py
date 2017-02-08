#!/usr/bin/env python3


def menu():
    """Print out list of options."""
    print("menu>>   <name>:add donor and donation   l:list donors   r:print report   t:thank you   h:help   q:quit")

donors = {
    'Donovan Leitch': [100, 20, 1000],
    'Stevie Nicks': [200, 500],
    'Ian Anderson': [190],
    'Mavis Staples': [170, 40, 130],
    'Suzanne Vega': [160, 300]
}


def thank_you():
    """Write a thank you letter."""
    full_name = input("(Donor full name) / (list) > ")

    if full_name == 'list'.lower():
        print("Donors:", end=' ')
        for key, value in donors.items():
            print(key, end=', ')
        print('\n')
        thank_you()
    elif full_name in donors:
        while True:
            new_donation = input("New donation amount > ")
            try:
                new_donation = int(new_donation)
                break
            except ValueError:
                print("Please enter a number.")
        donors[full_name].append(new_donation)
        print(donors)
        write_letter(full_name, new_donation)
    else:
        donors[full_name] = []
        while True:
            new_donation = input("New donation amount > ")
            try:
                new_donation = int(new_donation)
                break
            except ValueError:
                print("Please enter a number.")
        donors[full_name].append(new_donation)
        print(donors)


def write_letter(full_name, new_donation):
    """Compose and print thank you letter."""
    letter = '''
    Dear {},

    Thank you for your generous donation of ${}.
    Your gift makes a major impact on aspiring musicians in the Seattle area.

    Sincerely,
    Seattle Music Fund
    '''.format(full_name, str(new_donation))
    print(letter)
    menu()


def create_report():
    """Generate a report of donors and donation amounts."""
    donors_sorted = sorted(donors.items(),
                           key=lambda t: sum(t[1]), reverse=True)
    print("Donor Name          | Total Given | Num Gifts | Average Gift")

    for donor in donors_sorted:
        print(donor[0], end='   ')
        print('$' + str(sum(donor[1])), end='   ')
        print(len(donor[1]), end='   ')
        print('$' + str(round(float(sum(donor[1])/len(donor[1])), 2)))

    print('\n', end='')
    menu()


def add_donation(new_donor, new_amount):
    """Add donation entry into donors dictionary."""
    donors[new_donor] = [new_amount]

if __name__ == '__main__':
    menu()

    while True:
        user_input = input('mailroom>>   ')

        if user_input == 'q' or user_input == 'quit':
            break

        if user_input == 'l' or user_input == 'list donors':
            continue

        if user_input == 'r' or user_input == 'create report':
            create_report()
            continue

        if user_input == 't' or user_input == 'thank donors':
            thank_you()
            continue

        if user_input == 'h' or user_input == 'help':
            continue

        new_donor = user_input

        new_amount = int(input("mailroom >>   How much is {} donating? ".format(new_donor)))

        add_donation(new_donor, new_amount)