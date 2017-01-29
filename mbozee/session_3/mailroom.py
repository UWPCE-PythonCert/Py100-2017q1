#!/usr/bin/env python3

donors = {
    'Donovan Leitch': [100, 20, 150],
    'Stevie Nicks': [200, 80],
    'Ian Anderson': [190],
    'Mavis Staples': [170, 40, 130],
    'Suzanne Vega': [160, 30]
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
        new_donation = int(input("New donation amount > "))
        donors[full_name].append(new_donation)
        print(donors)
        write_letter(full_name, new_donation)
    else:
        donors[full_name] = []
        new_donation = int(input("New donation amount > "))
        donors[full_name].append(new_donation)
        print(donors)
        write_letter(full_name, new_donation)


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
    pass


def menu():
    """Give user choice of actions."""
    options = {1: 'Send a Thank You', 2: 'Create a Report', 3: 'quit'}
    choice = input("Choose an option:\n" + str(options) + " > ")

    if choice == str(1):
        thank_you()
    elif choice == str(2):
        print("Create a Report coming soon...")
    elif choice == str(3):
        pass
    else:
        menu()

menu()