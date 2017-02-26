'''
Session 3
Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each
The script should prompt the user (you) to choose from a menu of 3 actions: ‘Send a Thank You’ or ‘Create a Report’ or ‘quit’)

Session 4
Use dicts where appropriate
Write a full set of letters to everyone to individual files on disk
See if you can use a dict to switch between the users selections
Try to use a dict and the .format() method to do the letter as one big template – rather than building up a big string in parts.
'''


# I have reused a lot of code from a To Do list program I created in my Into to Python class.
# This has presented some challenges when trying to refactor the code

# -- Processing -- #
def initialize_donordb():
    donors = {
    'Ruby': [50, 100],
    'Khloe': [1000, 1500],
    'Sara': [2000, 2500, 3000],
    'Starla': [50],
    'Tim': [100]
    }
    #  print("this is my donor list", donors)
    return donors


def menu_options(): # Task 3
    """Make a function for the code that allows the user to Add or Remove tasks from the list,
    plus save the tasks in the List tasks-priorities using numbered choices."""
    print("""
        Please Select an option:
        1) Add a Donor/Donation
        2) View Donor List
        3) Print Report
        4) Send "Thank You"
        5) Save all tasks to the Donor file and exit!
        """)


def add_donation(db, donor, contribution):
    if donor in db.keys():
        db[donor].append(int(contribution))
    else:
        db[donor] = [int(contribution)]


def report_calcs(values):  # totally stole this from Rick
    donation_total = sum(values)
    num_gifts = len(values)
    average_gift = donation_total / num_gifts
    return str(donation_total), str(num_gifts), average_gift


def donor_report(db):  # totally stole this from Rick
    # Print a header
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print('------------------------------------------------------------------')
    # Print each row
    for names, values in db.items():
        donation_total, num_gifts, average_gift = report_calcs(values)

        print("{} | ${} | {} | ${:11,.2f}".format(
            names.ljust(25),  # Left justify the names
            donation_total.rjust(11),
            num_gifts.rjust(9),
            average_gift,  # Handle formatting in the format string
        ))


def thank_you(db):
    for names, values in db.items():
        donation_total = sum(values)
        print('Dear ' + names + ', \n')
        print('Thank you for you generous donation of $' + str(donation_total) + '.\n')
        print('Your continued support of my fundraising efforts for the Big Climb keeps me motivated. \n')
        print('Together we WILL find a cure for Blood related cancers! \n')
        print('Thank you, \n')
        print('Matt')


# -- Input/Output -- #


def main():
    """Coordinates I/O and actions"""
    try:
        donor_db = initialize_donordb()

        # Display all tasks to user
        # donor_report(gTodoTasks)

        # Display a menu of choices to the user
        # and Process user I/0
        while True:
            menu_options()
            str_choice = str(input("Which option would you like to perform? [1 to 5]"))
            # Need to add if/elif for adding donor/donation
            if str_choice == '1':    # 1) Add a new item.
                new_donor = str(input("What is the donor's name?"))
                contribution = int(input("What is the amount?"))
                add_donation(donor_db, new_donor, contribution)
                # donor_report(gTodoTasks)
                continue

            elif str_choice == '2':
                print(sorted(set(donor_db.keys())))

            elif str_choice == '3':    # Print Report
                donor_report(donor_db)
                continue
            elif str_choice == '4':
                thank_you(donor_db)
                continue
            else:  # Not working needs to go into a try block
                print("Please select a number from [1 to 5]")  # Message in case user enters the incorrect number
                # donor_report(gTodoTasks)
                continue
    except IOError as error:  # Handles any Python errors
        #print("Hmmm somthing isn't right...")
        #print("pythons error info: ")
        print(error)


# start the program
main()  # Call the Main function at the start of the script

