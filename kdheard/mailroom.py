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


def get_donor_name(input_name, unit_test=False):
    str(input_name)
    if input_name == "":
        return
    elif input_name == 'list':
        for donor_number, donor in db.items():
            print(donor['name'])

            #return True
        return
    elif input_name != 'list':
        # We will run a quick set of input validations on donor and donations
        if input_name.isdigit():
            print(Exception("You need to enter a name for your donor. You have entered a number."))
        else:
            if unit_test==False:
                donation = input("How much has this donor contributed? > ")
                get_donation(donation, input_name)
            elif unit_test==True:
                return True
        # ^ Check if string was entered for donor name


def get_donation(donation, input_name):

    try:
        int(donation)
    except ValueError as error:
        print("You need to enter a number. Error:{}".format(error))
        return
        # ^ Check of number was entered for donation
    if donation[0] is "-":
        print(Exception("STOP EMBEZZLING, JANET, THE BOARD IS ON TO YOU!"))
        return
        # ^ Check for negative donations
# Input validation is done, now we will pass input_name and donation into thank_you to be added into the DB
    thank_you(donation,input_name)


def generate_email(donation, input_name):
    print("\nGenerating e-mail...\n-------------------------")
    print(
        "Dear {}, \n\nThank you for your generous donation of ${}. With the help of contributions like yours, we can continue to"
        " \naid individuals who have mistakenly been added to NSA watchlists because of Autocorrect."
        "\n\nYours truly: \nThe Director".format(input_name, donation))


def thank_you(donation, input_name):
    global new_donor_number
    input_name = str(input_name)
    donation = int(donation)
    for donor_number, donors in db.items():
        if input_name.title() == str(donors['name'].title()):
            donors['donations'].append(donation)
            generate_email(donation, input_name)
            return
    for donor_number, donors in db.items():
        if input_name.title() != donors['name']:
            global new_donor_number
            new_donor = 'new_donor{}'.format(new_donor_number)
            db[new_donor] = {}
            db[new_donor]['name'] = input_name.title()
            db[new_donor]['donations'] = []
            db[new_donor]['donations'].append(donation)
            new_donor_number = new_donor_number + 1
            generate_email(donation, input_name)
            break


def create_report():
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
    return


def main(response=None):
    if response != None:
        pass
    else:
        response = input("\nWelcome to Mailroom. \n\nYou have three options: \n(1.) Send a Thank You \n(2.) Create a Report \n(3.) Quit \n\nWhat would you like to do? > ")
    try:
        if int(response) == 1:
            input_name = input("Type 'list' to see existing donors, or type the full name of a donor. Or, press ENTER to return to the main menu. > ")
            get_donor_name(input_name)
        elif int(response) == 2:
            create_report()
        elif int(response) == 3:
            print("\nThank you for using Mailroom. Exiting program.")
            exit()
        else:
            print(Exception("That isn't a valid input. Try again."))
            return
    except ValueError as error:
        print("\nThat isn't a valid input. Try again. \nError:{}".format(error))







if __name__ == "__main__":
    while True:
        main()
