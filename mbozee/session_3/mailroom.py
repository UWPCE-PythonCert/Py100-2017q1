#!/usr/bin/env python3

donors = {
    'Donovan Leitch': [100, 20, 1000],
    'Stevie Nicks': [200, 500],
    'Ian Anderson': [190],
    'Mavis Staples': [170, 40, 130],
    'Suzanne Vega': [160, 300]
}


def menu():
    """Give user choice of actions."""
    for keys, values in donors.items():
        print(keys, end=', ')
    print(end='\n')
    options = {1: 'Send a Thank You', 2: 'Create a Report', 3: 'quit'}
    choice = input("Choose an option:\n" + str(options) + " > ")

    while choice != '3' and choice != 'quit'.lower():

        if choice == str(1):
            thank_you()
        elif choice == str(2):
            create_report()
        else:
            menu()
        break


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
    donors_sorted = sorted(donors.items(),
                           key=lambda t: sum(t[1]), reverse=True)
<<<<<<< HEAD
    print("Donor Name          | Total Given | Num Gifts | Average Gift")

    for donor in donors_sorted:
        print(donor[0], end='   ')
        print('$' + str(sum(donor[1])), end='   ')
        print(len(donor[1]), end='   ')
        print('$' + str(round(float(sum(donor[1])/len(donor[1])), 2)))

    print('\n', end='')
    menu()

if __name__ == '__main__':
    menu()
=======
    for donor in donors_sorted:
        print(donor[0], end='   ')
        print('$  ' + str(sum(donor[1])), end='   ')
        print("Donations: " + str(len(donor[1])))
        print("Average donation: $" + str(round(float(sum(donor[1])/len(donor[1])), 2)))


menu()
>>>>>>> b7eb1055c08ee6963ef92f891c8583ea5af36bb2
