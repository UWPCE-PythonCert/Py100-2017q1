#!/usr/bin/env python3

options = ['<name>:add donor and donation',
           'l:list donors',
           'r:print report ',
           't:thank you',
           'h:help',
           'q:quit']

donors = {
    'Donovan Leitch': [100, 20, 1000],
    'Stevie Nicks': [200, 500],
    'Ian Anderson': [190],
    'Mavis Staples': [170, 40, 130],
    'Suzanne Vega': [160, 300]}


class Donor:
    '''Donor stuff.'''
    def __init__(self, donor_name):
        self.donor_name = ''

    def list_donors(self):
        """Print a list of donor names."""
        for donor_name in donors:
            print(donor_name)


class Report:
    '''Report stuff.'''
    def __init__(self, report):
        self.report = ''

    def print_report(self):
        """Generate a report of donors and donation amounts."""
        donors_sorted = sorted(donors.items(),
                               key=lambda t: sum(t[1]), reverse=True)

        print("Donor Name                | Total Given | Num Gifts | Avg Gift")

        for donor in donors_sorted:
            print("{} | {} | {} | {}".format(
                donor[0].ljust(25),
                str(sum(donor[1])).rjust(11),
                str(len(donor[1])).rjust(9),
                str(round(sum(donor[1]) / len(donor[1]))).rjust(8)
            ))

        print('\n', end='')


def menu():
    '''Provides user with list of options.'''

    while True:
        choice = input('Choose an action {}: '.format(options))

        if choice == 'q' or choice == 'quit':
            break

        if choice == 'l' or choice == 'list donors':
            donor = Donor(None)
            donor.list_donors()
            continue

        if choice == 'r' or choice == 'print report':
            report = Report(None)
            report.print_report()
            continue

        if choice == 't' or choice == 'thank donors':
            entry = [thank_you(name, sum(value)) for name, value in donors.items()]
            continue

        if choice == 'h' or choice == 'help':
            help()
            continue


def main():
    '''Calls menu function.'''
    menu()

if __name__ == '__main__':
    main()