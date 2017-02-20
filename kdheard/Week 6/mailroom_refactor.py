#!/usr/bin/env python3

from statistics import mean
import string

db = {
    'donor1': {'name': 'Ayn Rand', 'donations': [1000]},
    'donor2': {'name': 'William Gibson', 'donations': [1000, 5000, 500]},
    'donor3': {'name': 'Neal Stephenson', 'donations': [10, 100, 1000]},
    'donor4': {'name': 'George Orwell', 'donations': [19, 84]},
    'donor5': {'name': 'Aldous Huxley', 'donations': [600]},
}

#todo refactor around not calling main anymore
#todo wrap while true around the main menu to replace return_prompt
#todo parameterize all the defs
#todo use safe_input type thing to determine what's being validate it and validate it before passing it into the program (maybe use class?)
#todo SetUp method in py.test       ~ can replace mock possibly

class mailroom(object):

        def get_donor_name(self, input_name):
            if input_name == "":
                exit()
            elif input_name == 'list':
                for donor_number, donor in db.items():
                    print(donor['name'])
            elif input_name != 'list':
                # We will run a quick set of input validations on donor and donations
                if input_name.isdigit():
                    print(Exception("You need to enter a name for your donor. You have entered a number."))
                else:
                    pass
                # ^ Check if string was entered for donor name

        def get_donation(self, donation):
                try:
                    int(donation) % 1 == 0
                except ValueError as error:
                    print("You need to enter a number. Error:{}".format(error))
                    # ^ Check of number was entered for donation
                if donation[0] is "-":
                    print(Exception("STOP EMBEZZLING, JANET, THE BOARD IS ON TO YOU!"))
                    # ^ Check for negative donations
        # Input validation is done, now we will pass input_name and donation into thank_you to be added into the DB

        def generate_email(self, donation, input_name):
            print("\nGenerating e-mail...\n-------------------------")
            print(
                "Dear {}, \n\nThank you for your generous donation of ${}. With the help of contributions like yours, we can continue to"
                " \naid individuals who have mistakenly been added to NSA watchlists because of Autocorrect."
                "\n\nYours truly: \nThe Director".format(input_name, donation))

        def thank_you(self, input_name, donation):
                input_name = str(input_name)
                donation = int(donation)
                for donor_number, donors in db.items():
                    if input_name.title() == donors['name']:
                        donors['donations'].append(donation)
                    elif input_name.title() != donors['name']:
                        global new_donor_number
                        new_donor = 'new_donor{}'.format(new_donor_number)

                        db[new_donor] = [new_donor]['name'] = input_name.title()
                        db[new_donor]['donations'] = []
                        db[new_donor]['donations'].append(donation)
                        new_donor_number = new_donor_number + 1
                self.generate_email(donation, input_name)

        def create_report(self):
            print("Name                 Total Donations   No. of Donations   Avg Donation")
            print(
                "--------------------------------------------------------------------------------------------")
            for donor_number, donors in db.items():
                list_name = donors['name']
                total_donations = 0
                for donation in donors['donations']:
                    total_donations += donation
                number_of_donations = len(donors['donations'])
                average_donations = mean(donors['donations'])
                print("{0:20}| ${1:15}| {2:15}| ${3:.2f}".format(list_name, total_donations, number_of_donations, average_donations))

        def main(self):
            print("Welcome to Mailroom. \n\nYou have three options: \n(1.) Send a Thank You \n(2.) Create a Report \n(3.) Quit")

            response = input("\nWhat would you like to do? > ")
            try:
                if int(response) == 1:
                    input_name = input("Type 'list' to see existing donors, or type the full name of a donor. Or, press ENTER to return to the main menu. > ")
                    donation = input("How much has this donor contributed? > ")
                    self.get_donor_name(input_name)
                    self.get_donation(donation)
                elif int(response) == 2:
                    self.create_report()
                elif int(response) == 3:
                    print("\nThank you for using Mailroom. Exiting program.")
                else:
                    print(Exception("That isn't a valid input. Try again."))
                    return False
            except ValueError as error:
                print("\nThat isn't a valid input. Try again. \nError:{}".format(error))
                return False

        def __init__(self):
            while True:
                self.main()




if __name__ == "__main__":
    mailroom()