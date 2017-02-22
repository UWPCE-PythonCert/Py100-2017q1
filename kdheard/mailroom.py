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

new_donor_number = 1


class mailroom(object):

        def get_donor_name(self, input_name, unit_test = False):
            str(input_name)
            if input_name == "":
                if unit_test == True:
                    return True
                else:
                    return
            elif input_name == 'list':
                for donor_number, donor in db.items():
                    print(donor['name'])
                    return True
            elif input_name != 'list':
                # We will run a quick set of input validations on donor and donations
                if input_name.isdigit():
                    print(Exception("You need to enter a name for your donor. You have entered a number."))
                    return False
                else:
                    if unit_test == True:
                        return True
                    else:
                        donation = input("How much has this donor contributed? > ")
                        self.get_donation(donation,input_name)
                # ^ Check if string was entered for donor name

        def get_donation(self,donation,input_name, unit_test = False):
            try:
                int(donation) % 1 == 0
                if unit_test == True:
                    return True
            except ValueError as error:
                print("You need to enter a number. Error:{}".format(error))
                if unit_test == True:
                    return False
                else:
                    return
                # ^ Check of number was entered for donation
            if donation[0] is "-":
                print(Exception("STOP EMBEZZLING, JANET, THE BOARD IS ON TO YOU!"))
                if unit_test == True:
                    return False
                else:
                    return
                # ^ Check for negative donations
        # Input validation is done, now we will pass input_name and donation into thank_you to be added into the DB
            self.thank_you(input_name,donation)


        def generate_email(self, donation, input_name):
            print("\nGenerating e-mail...\n-------------------------")
            print(
                "Dear {}, \n\nThank you for your generous donation of ${}. With the help of contributions like yours, we can continue to"
                " \naid individuals who have mistakenly been added to NSA watchlists because of Autocorrect."
                "\n\nYours truly: \nThe Director".format(input_name, donation))

        def thank_you(self, input_name, donation):
            global new_donor_number
            input_name = str(input_name)
            donation = int(donation)
            for donor_number, donors in db.items():
                if str(input_name.title()) == str(donors['name']):
                    donors['donations'].append(donation)
                    break
                elif input_name.title() != donors['name']:
                    global new_donor_number
                    new_donor = 'new_donor{}'.format(new_donor_number)
                    db[new_donor] = {}
                    db[new_donor]['name'] = input_name.title()
                    db[new_donor]['donations'] = []
                    db[new_donor]['donations'].append(donation)
                    new_donor_number = new_donor_number + 1
                    break
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

        def main(self, response=input("\nWelcome to Mailroom. \n\nYou have three options: \n(1.) Send a Thank You \n(2.) Create a Report \n(3.) Quit \n\nWhat would you like to do? > ")):
            try:
                if int(response) == 1:
                    input_name = input("Type 'list' to see existing donors, or type the full name of a donor. Or, press ENTER to return to the main menu. > ")
                    self.get_donor_name(input_name)
                elif int(response) == 2:
                    self.create_report()
                elif int(response) == 3:
                    print("\nThank you for using Mailroom. Exiting program.")
                else:
                    print(Exception("That isn't a valid input. Try again."))
            except ValueError as error:
                print("\nThat isn't a valid input. Try again. \nError:{}".format(error))

        def __init__(self):
            while True:
                self.main()




