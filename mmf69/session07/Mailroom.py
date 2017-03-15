#!/usr/bin/python

from prettytable import PrettyTable
import sqlite3
import locale

locale.setlocale(locale.LC_ALL, '')
'English_United States.1252'
locale.currency(188518982.18)
'$188518982.18'

conn = sqlite3.connect('donor.db')


# print("Opened database successfully")


def donor_list():
    print("********DONORS***********")
    cursor = conn.execute("SELECT DISTINCT DONOR_ID as 'Donor ID',"
                          "DONOR_NAME as 'Donor Name' from donors order by DONOR_ID")
    col_names = [cn[0] for cn in cursor.description]
    rows = cursor.fetchall()
    x = PrettyTable(col_names)
    x.align[col_names[0]] = "c"
    x.align[col_names[1]] = "l"
    x.padding_width = 1
    for row in rows:
        x.add_row(row)
    print(x)


def donor_report():
    print("*********************************DONOR REPORT***************************************")
    cursor = conn.execute("SELECT DONOR_ID as 'Donor ID',DONOR_NAME as 'Donor Name',"
                          "total(DONATION_AMOUNT) AS 'Total Donations',"
                          "count(DONOR_ID) AS 'Number of Donations',"
                          "total(DONATION_AMOUNT)/count(DONOR_ID) AS 'Average Donation'"
                          " from donors group by DONOR_ID,DONOR_NAME")
    col_names = [cn[0] for cn in cursor.description]
    rows = cursor.fetchall()
    x = PrettyTable(col_names)
    x.align[col_names[1]] = "l"
    x.align[col_names[2]] = "r"
    x.align[col_names[3]] = "c"
    x.align[col_names[4]] = "r"
    x.padding_width = 1
    for row in rows:
        x.add_row(row)
    print(x)


def thank_you():
    cursor = conn.execute("SELECT DONOR_NAME as 'Donor Name',"
                          "total(DONATION_AMOUNT) AS 'Total Donations'"
                          " from donors group by DONOR_ID,DONOR_NAME")
    rows = cursor.fetchall()
    for row in rows:
        with open('mailroom-thankyou-{}.txt'.format(row[0]), 'w') as f:
            f.write('Dear ' + str(row[0]) + ', \n'
                    'Thank you for you generous donation of ' +
                    locale.currency(row[1], 'True') + '.\n'
                    'Your continued support of my fundraising efforts for the Big Climb keeps me motivated. \n'
                    'Together we WILL find a cure for Blood Related Cancers! \n'
                    'Thank you, \n'
                    'Matt')


def list_donor_files():
    import glob
    print(glob.glob("mailroom-thankyou-*.txt"))


def menu_options():
    print("""
        Please Select an option:
        1) Add a Donor/Donation
        2) View Donor List
        3) Print Report
        4) Send "Thank You"
        5) Save all tasks to the Donor file and exit!
        """)


def main():
    """Coordinates I/O and actions"""
    try:
        # Display a menu of choices to the user
        # and Process user I/0
        while True:
            menu_options()
            str_choice = str(input("Which option would you like to perform? [1 to 5]"))
            # Need to add if/elif for adding donor/donation
            if str_choice == '1':  # 1) Add a new item.
                new_donor = str(input("What is the donor's name?"))
                contribution = int(input("What is the amount?"))
                add_donation(donor_db, new_donor, contribution)
                # donor_report(gTodoTasks)
                continue

            elif str_choice == '2':  # Print List
                donor_list()

            elif str_choice == '3':  # Print Report
                donor_report()
                continue
            elif str_choice == '4':
                list_donor_files()
                continue
            elif str_choice == '5':
                # Save (commit) the changes
                conn.commit()
                conn.close()
                print("Operation done successfully")
                exit()
            else:
                print(Exception(
                    "\nThat isn't a valid input. Please select a number from [1 to 5]"))  # Message in case user enters the incorrect number
                # donor_report(gTodoTasks)
                continue
    except IOError as error:  # Handles any Python errors
        print("Hmmm something isn't right...")
        print("pythons error info: ")
        print(error)


# start the program
main()  # Call the Main function at the start of the script
