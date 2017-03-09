#!/usr/bin/env python3
import sys
from collections import OrderedDict

from donor import Donor


class mailroom_oo():
    def __init__(self):
        self.donors = []
        self.db_filename = './initial_donor_list.csv'
        self.menu_dict = {"1": self.send_a_thank_you, "2": self.create_a_report, "3": self.quit_app}
        self.menu_items = OrderedDict([("1", "Send a a Thank you note"),
                                       ("2", "Create a report"),
                                       ("3", "Quit")])
        self.load_donor_list()
        self.display_menu()

    def display_menu(self):
        while True:
            print("Enter string from items below:")
            [print("{}.  {}".format(key, value)) for key, value in self.menu_items.items()]
            response = self.safe_input("> ")
            if response is None:
                self.quit_app()
            if response in self.menu_dict:
                self.menu_dict[response]()
            else:
                print("Invalid entry.  Try again.\n")

    def load_donor_list(self):
        with open(self.db_filename, 'r') as f:
            for line in f:
                read_data = line.split(',')
                donor = Donor(read_data[0].strip(), read_data[1].strip())
                for i in range(2, len(read_data)):
                    donor.add_donation(float(read_data[i]))
                self.donors.append(donor)
        f.close()

    def write_thank_you_note(self, donor_index):
        donor = self.donors[donor_index]
        # f = open('./Thank_you_to_{}_{}.txt'.format(donor.first_name, donor.last_name), 'w')
        lines = ["To {} {}:\n".format(donor.first_name, donor.last_name), "\n",
                 "Thank you for you generous donation of $%.2f\n" % donor.donations[-1], "\n",
                 "Sincerely,\n", "Gnrc Foundation\n"]
        # f.writelines(lines)
        # f.close()
        # print(f.name + " saved")
        print("".join(lines))
        print("")

    def create_a_report(self):
        indices = self.sort_donors()
        self.print_a_report(indices)

    def print_a_report(self, donor_index):
        header = 'Donor Name                | Total Given | Num Gifts | Average Gift'
        top_line = '-' * len(header)
        print(header)
        print(top_line)
        for i in donor_index:
            self.donors[i].print_donor_contributions()
        print()

    def send_a_thank_you(self):
        donor_names = self.get_donor_names_list()
        print("Hit 'Enter' at any prompt to return to main menu")
        response = self.safe_input("Enter Name of donor or 'l' for list > ")
        if response is None:
            self.quit_app()
        if response[0].lower() == "l":
            print("\n".join(donor_names))
            print()
            self.send_a_thank_you()
        elif response in donor_names:
            donor_index = donor_names.index(response)
            self.add_new_donation(donor_index)
            self.print_a_report([donor_index])
            self.write_thank_you_note(donor_index)
        elif response != "":
            if not self.is_valid_new_donor_name(response):
                self.send_a_thank_you()
            self.add_a_donor(response)
            donor_names = self.get_donor_names_list()
            donor_index = donor_names.index(response)
            self.add_new_donation(donor_index)
            self.print_a_report([donor_index])
            self.write_thank_you_note(donor_index)
        else:
            self.display_menu()

    def get_donor_names_list(self):
        return [donor.get_donor_name() for donor in self.donors]

    def add_a_donor(self, new_donor):
        donor_name = new_donor.split()
        self.donors.append(Donor(donor_name[0], donor_name[1]))

    def sort_donors(self):
        """
        Sort the donors list by total overall donation from most to least.
        Returns an array index
        """
        sort_indices = [i[0] for i in sorted(enumerate(self.donors), key=lambda x: x[1], reverse=True)]
        return sort_indices

    def add_new_donation(self, donor_index):
        while True:
            response = self.safe_input("Enter donation amount > ")
            if response is None:  # escape code entered
                self.quit_app()
            elif response == "":
                self.display_menu()
            elif not response.isnumeric():
                print("Invalid Input")
            else:
                self.donors[donor_index].add_donation(float(response))
                break

    @staticmethod
    def quit_app():
        print("Quitting!")
        sys.exit()

    @staticmethod
    def safe_input(prompt):
        try:
            return input(prompt)
        except (EOFError, KeyboardInterrupt):
            return None

    @staticmethod
    def is_valid_new_donor_name(new_donor):
        donor_name = new_donor.split()
        if len(donor_name) != 2:
            print("Invalid input:  Must type a first name and last name!")
            print()
            return False
        return True


mailroom_oo()
