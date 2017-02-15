#!/usr/bin/env python3

# ______________________________________________________________________________________________________________________
# IMPORT DEPENDENT MODULES
import pickle
import sys

# ______________________________________________________________________________________________________________________
# DEFINE GLOBAL VARIABLES
donor_data_file_name = '/home/vagrant/PycharmProjects/git/Py100-2017q1/ejviola/DonorData.pkl'
# Open donor data, read donor data into a new list of dicts, close donor data file
try:
    donor_data_file = open(donor_data_file_name, 'rb')
    donor_data = pickle.load(donor_data_file)
    donor_data_file.close()
    # Create new donor_list of unique donors based on donor_data
    donor_list = []
    for row in donor_data:
        if row['Name'] not in donor_list:
            donor_list.append(row['Name'])
    cause_list = []
    for row in donor_data:
        if row['Cause'] not in cause_list:
            cause_list.append(row['Cause'])
    report = []

except (EOFError, FileNotFoundError) as e:
    with open(donor_data_file_name, 'wb') as donor_data_file:
        pickle.dump([{'Name': "Bill Gates", 'Amount': 115000000, 'Date': "August 1, 1991",
                                    'Cause': 'combat homelessness.'}, {'Name': "Bill Gates", 'Amount': 9176200, 'Date': "January 3, 1999",
                                    'Cause': "support global literacy."}, {'Name': "Bill Gates", 'Amount': 115000000, 'Date': "September 1, 1999",
                                    'Cause': "engage in local outreach efforts to raise awareness about homelessness."}, {'Name': "Paul Allen", 'Amount': 3150000, 'Date': "November 12, 2000",
                                    'Cause': "support global literacy."}, {'Name': "Bill Gates", 'Amount': 115000000, 'Date': "August 17, 2001",
                                    'Cause': "combat homelessness."}], donor_data_file)
    print(e)
    print("Wrote 5 starter records to " + donor_data_file_name + " and successfully exited.")
    sys.exit()



# ______________________________________________________________________________________________________________________
# PROCESSING
# Define function to write donor data to the file
def write_donor_data():
    with open(donor_data_file_name, 'wb') as donor_data_file :
        pickle.dump(donor_data, donor_data_file)

# Define a function to send a thank you
def send_thank_you():
    user_thank_you_input = 0
    user_thank_you_input = str(input("\nType a name to send a thank you,\nenter 'list' to see a list of unique donors,\nor enter 'back' to go back\n"))
    if user_thank_you_input.lower() == 'list':
        print(donor_list)
    elif user_thank_you_input == 'back':
        print("Returning to main menu")
    else:
        thank_you_path = str(
            input("Are you thanking " + str(user_thank_you_input) + " for a new donation, or sending a followup thank-you for an old donation? Enter new or old:\n"))
        if thank_you_path == str("new"):
            # If it is a new donation, send a thank you based on the details of that donation
            # While loop to make sure the amount donated is valid
            while True:
                try:
                    amount_donated = input("Please enter the amount " + user_thank_you_input + " donated (e.g. '10000'):\n")
                    amount_donated = float(amount_donated)
                    break
                except ValueError:
                    print("You did not enter a valid amount.")
                    pass
            donation_date = str(input("Please enter the date the donation was made (e.g. 'January 1, 2017': \n"))
            donation_cause = str(input(
                "Please enter the cause that the donation will support (e.g. 'increase rural broadband access'\n"))
            # If the cause isn't already in the cause list, add it
            if donation_cause not in cause_list:
                cause_list.append(donation_cause)
            new_donation = {'Name': user_thank_you_input, 'Amount': amount_donated, 'Date': donation_date,
                            'Cause': donation_cause}
            donor_data.append(new_donation)
            # Ask the user if they would like to save the data
            write_choice = input("Would you like to save this donation? Enter y/n:\n")
            if write_choice == str("y"):
                write_donor_data()
                # If it is a new donor, also add them to donor_list
                if user_thank_you_input not in donor_list:
                    donor_list.append(user_thank_you_input)
            # Print Thank You
            print("Dear " + user_thank_you_input + ",")
            print("\tThank you for your generous donation of $" + str(amount_donated) + ". Your contribution well help us " + str(donation_cause) + ".")
            print("We look forward to pursuing this important mission, and hope that you will continue to support our efforts as we pursue our other goals.")
            print("\n\nThank you again,")
            print("\tEric Viola")
        elif thank_you_path == str("old"):
            # If it is not a new donation, thank them based on a generic letter
            print("Dear " + user_thank_you_input + ",")
            print(
                "\tThank you again for your generous donation. Philanthropists like you empower our organization to deliver tangible outcomes across the globe. \nYour contribution will help our organization as we pursue our strategic missions, such as: ")
            counter = 0
            # The generic letter lists all the causes that have been funded so far (not ranked at all)
            for cause in cause_list:
                counter +=1
                print("\t\t"+str(counter)+") "+cause.title())
            print("\n\nThank you again for supporting our efforts,")
            print("\t Eric Viola")
        # Throw an error if no valid input was given and return to main menu (progress is not saved)
        else:
            print("You did not enter a valid command, returning to main menu")


# Define a function to generate a report
def generate_report():
    report = []
    for donor in donor_list:
        donation_sum = 0
        donation_count = 0
        for row in donor_data:
            if donor == row['Name']:
                donation_sum += row['Amount']
                donation_count += 1
        new_row = [donation_sum, donor, donation_count, donation_sum, round(donation_sum/donation_count, 0)]
        report.append(new_row)
    report.sort(reverse=True)
    print("Donor", 25*" ", " Donations", "   Total Donated", "   Average Donation")
    for report_row in report:
        print(report_row[1], (30-len(report_row[1]))*" ", (9-len(str(report_row[2])))*" ", report_row[2], "  $", (11-len(str(report_row[3])))*" ", report_row[3], "   $", (13-len(str(report_row[4])))*" ", report_row[4])
    print("\nEnd of Report")

# Define a function to give the user options between the existing functions
def user_interface():
    user_input = 0
    # While loop to match user input with relevant function
    while user_input != 3:
        try:
            user_input = int(input("\nUser Options:\n1) Send a Thank You\n2) View Donor Report\n3) Quit \nEnter a number:\n"))
            if int(user_input) in [1, 2, 3]:
                #user_input = int(user_input)
                if user_input == 1:
                    print('\nYou chose to send a thank you\n')
                    send_thank_you()
                elif user_input == 2:
                    print('\nYou chose to view a report\n')
                    generate_report()
            else:
                print("\nPlease enter 1, 2, or 3\n")
        except:
            print("\nPlease enter 1, 2, or 3\n")
    print("\nSuccessfully Exited\n")

# ______________________________________________________________________________________________________________________
# INPUT AND OUTPUT
user_interface()