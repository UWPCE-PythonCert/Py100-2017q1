#!/usr/bin/env python3

from statistics import mean

db = {
    'donor1': {'name': 'Ayn Rand', 'donations': [1000]},
    'donor2': {'name': 'William Gibson', 'donations': [1000, 5000, 500]},
    'donor3': {'name': 'Neal Stephenson', 'donations': [10, 100, 1000]},
    'donor4': {'name': 'George Orwell', 'donations': [19, 84]},
    'donor5': {'name': 'Aldous Huxley', 'donations': [600]},
}

new_donor_number = 1

def return_prompt():
        prompt = input("\nPress enter to return to main menu.\n")
        main()


def thank_you():

    input_name = input("Type 'list' to see existing donors, or type the full name of a donor. Or, press ENTER to return to the main menu. > ")
    str(input_name)
    if input_name == "":
        main()
    elif input_name == 'list':
        for donor_number, donor in db.items():
            print(donor['name'])
        return_prompt()
    elif input_name != 'list':

        donation = input("How much has this donor contributed? > ")
        donation = int(donation)
        for donor_number, donors in db.items():
            if input_name == donors['name']:
                donors['donations'].append(donation)
                generate_email(donation, donors['name'])
        else:
            global new_donor_number
            new_donor = 'new_donor{}'.format(new_donor_number)
            db[new_donor] = {}
            db[new_donor]['name'] = input_name
            db[new_donor]['donations'] = []
            db[new_donor]['donations'].append(donation)
            new_donor_number = new_donor_number + 1
            print(new_donor_number)
            print(db)
            generate_email(donation, input_name)


def generate_email(donation, input_name):
    print("\nGenerating e-mail...\n-------------------------")
    print("Dear {}, \n\nThank you for your generous donation of ${}. With the help of contributions like yours, we can continue to"
            " \naid individuals who have mistakenly been added to NSA watchlists because of Autocorrect."
            "\n\nYours truly: \nThe Director".format(input_name,donation))

    return_prompt()

def create_report():

    print("Name                 Total Donations   No. of Donations   Avg Donation")
    print("--------------------------------------------------------------------------------------------")
    for donor_number, donors in db.items():
        list_name = donors['name']
        total_donations = 0
        for donation in donors['donations']:
            total_donations += donation
        number_of_donations = len(donors['donations'])
        average_donations = mean(donors['donations'])
        print("{0:20}| ${1:15}| {2:15}| ${3:.2f}".format(list_name, total_donations, number_of_donations, average_donations))
    return_prompt()


def main():
        print("Welcome to Mailroom. \n\nYou have three options: \n(1.) Send a Thank You \n(2.) Create a Report \n(3.) Quit")
        response = input("\nWhat would you like to do? > ")
        if int(response) == 1:
            thank_you()
        elif int(response) == 2:
            create_report()
        elif int(response) == 3:
            print("\nThank you for using Mailroom. Exiting program.")
            pass

if __name__ == "__main__":
   main()
