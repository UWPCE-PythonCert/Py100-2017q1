#!/usr/bin/env python3

from statistics import mean

db = {
    'donor1': {'name': 'Ayn Rand', 'donations': {1000}},
    'donor2': {'name': 'William Gibson', 'donations': {1000, 5000, 500}},
    'donor3': {'name': 'Neal Stephenson', 'donations': {10, 100, 1000}},
    'donor4': {'name': 'George Orwell', 'donations': {19, 84}},
    'donor5': {'name': 'Aldous Huxley', 'donations':{600}}
}

def return_prompt():
        prompt = input("\nPress enter to return to main menu.\n")
        main()


def thank_you():

    input_name = input("Type 'list' to see existing donors, or type the full name of a donor. Or, press ENTER to return to the main menu. > ")
    str(input_name)
    if input_name == "":
        main()
    elif input_name == 'list':
        for donors in db:
            print(db[str(donors)]['name'])
        return_prompt()
    elif input_name != 'list':
        donation = input("How much has this donor contributed? > ")
        for donors in db:
            str(donors)
            while input_name == db[donors]['name']:
                db[donors]['donations'].add(donation)
                break
            else:
                db['new_donor'] = {}
                db['new_donor']['name'] = input_name
                db['new_donor']['donations'] = donation
                print(db)
                break



    print("\nGenerating e-mail...\n-------------------------")
    print("Dear {}, \n\nThank you for your generous donation of ${}. With the help of contributions like yours, we can continue to"
            " \naid individuals who have mistakenly been added to NSA watchlists because of Autocorrect."
            "\n\nYours truly: \nThe Director".format(str(input_name),donation))

    return_prompt()

def create_report():
    width = 20

    print("Name                  Total Donations       Number of Donations    Average Donation")
    print("--------------------------------------------------------------------------------------------")
    for donors in db:
        str(donors)
        list_name = db[donors]['name']
        total_donations = sum(db[donors]['donations'])
        number_of_donations = len(db[donors]['donations'])
        average_donations = mean(db[donors]['donations'])
        print("{}| ${}| {}| ${:.2f}".format(list_name.ljust(width),str(total_donations).ljust(width),str(number_of_donations).ljust(width),average_donations))
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

