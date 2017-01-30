#!/usr/bin/env python3
db = {
    'donor1': {'name': 'Zero Crash', 'donations': {13.37}},
    'donor2': {'name': 'William Gibson', 'donations': {1000, 5000, 500}},
    'donor3': {'name': 'Neal Stephenson', 'donations': {10, 100, 1000}},
    'donor4': {'name': 'George Orwell', 'donations': {19, 84}},
    'donor5': {'name': 'Aldous Huxley', 'donations':{600}}
}

def return_prompt():
    prompt = input("Press 1 to return to main menu. Press 2 to quit.")
    if int(prompt) == 1:
        main()
    if int(prompt) == 2:
        quit()


def thank_you():
    name = input("Type 'list' to see existing donors, or type the full name of a donor > ")
    if name == 'list':
        for donors in db:
            print(db[str(donors)]['name'])
    if name != 'list':
        for donors in db:

    #todo search list for name (I'm guessing similar to listlab?)
    #todo if name not in list, then add name and donation to list
    donation = input("How much has this donor contributed? > ")
    print("Generating e-mail...\n -------------------------")
    print("Dear {}, \n\n Thank you for your generous donation of ${0:.2f}. With the help of contributions like yours, we can continue to"
          "aid individuals who have mistakenly been added to NSA watchlists because of Autocorrect. The fact that such a phenomenon exists is a"
          "ducking serial problematic and with your cornrowed generosity, we can pursuit our goalpost of helping these people."
          "\n\n Yours truly: \n The Director"
          "\n(Sent from Android Mobile)".format(name,donation))
    return_prompt()

def create_report():
    print("Name            Total Donations             Number of Donations             Average Donation")
    print("--------------------------------------------------------------------------------------------")
    for donors in db:
        list_name = db[str(donors)]['name']
       # total_donations = db[str(donors)][]
        #todo sum all the entries in the dict together
        number_of_donations = len(db[str(donors)]['donations'])
        #average_donations = #todo find function that averages all ints in a dict
        print("{}           {}            {}             {}".format(list_name,total_donations,number_of_donations,average_donations))
    return_prompt()

def quit():
    print("\nThank you for using Mailroom. Exiting program.")

def main():
        print("Welcome to Mailroom. \n\nYou have three options: \n(1.) Send a Thank You \n(2.) Create a Report \n(3.) Quit")
        response = input("\nWhat would you like to do? > ")
        if int(response) == 1:
            thank_you()
        if int(response) == 2:
            create_report()
        if int(response) == 3:
            quit()





if __name__ == "__main__":
   main()

