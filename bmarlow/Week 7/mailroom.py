#!/usr/bin/env python3

import os
import operator
import math

#build our initial dictionary
donors = {
    'Ricky': [1000],
    'Bobby': [1100, 2200],
    'Hansel': [5000, 6000, 7000],
    'Mr. Burgandy': [1, 2, 3, 4],
    'Austin': [123, 4567, 78, 99, 100],
    'Dale': [14, 234, 878, 345, 345, 234],
}



class utilities:
    
    
    def clear():
        """cross-platform screen clear, for prettiness"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def safeinput(inputstring):
        """function for input that catches EOF and Keyboard Interrupts"""
        # you'll quit my program how I tell you!
        try:
            data = input(inputstring + '\n')
            return data
        except (EOFError, KeyboardInterrupt):
            utilities.clear()
            main()
    def isnan(num):
        print(num)
        return math.isnan(num)


class mailroom:
    
    # build a menu for use
    def menu():
        """function for the main menu"""
        print('Please make a selection from the menu items below\n')
        print('1.  Send a Thank You Note\n')
        print('2.  Create a report\n')
        print('Press "q" to quit\n')
        selection = utilities.safeinput('')
        utilities.clear()
        if selection == '1':
            mailroom.names()
        elif selection == '2':
            mailroom.printreport()
        elif selection == 'q':
            print('exiting...')
        else:
            print(selection + ' is not a valid selection, please try again. \n')
            mailroom.menu()
            exit(0)
    
    def names():
        """function for looking up/listing/adding new donors"""
        name = utilities.safeinput('Please enter a name, or type "list" to view a list of available names (case sensitive):\n')
        utilities.clear()
        # if the name exists in our dictionary, use it
        if mailroom.namecheck(name):
            donations = donors[name]
            mailroom.nameselect(name, donations)
            mailroom.menu()
        # you want a list of names? you got it
        elif name == 'list':
            utilities.clear()
            mailroom.namelist()
            utilities.clear()
            mailroom.names()
        # you can't have a blank name silly
        elif name == '':
            utilities.clear()
            mailroom.names()
        # add the new person to the dictionary
        else:
            mailroom.createnewname(name)
            donations = mailroom.getdonations(name)
            mailroom.nameselect(name, donations)
            mailroom.menu()

    def namelist():
        namelist = []
        for key in donors.keys():
            print(key)
            namelist.append(key)
        print('')
        utilities.safeinput('Press Enter to COntinue')
        return namelist

    def namecheck(name):
        """function for checking if a donor is in the dictionary"""
        if name in donors.keys():
            return True
        else:
            return False

    def createnewname(name):
        """function to add a new name to the donors list"""
        newname = {name: []}
        donors.update(newname)
        donorlist = []
        for key in donors.keys():
            donorlist.append(key)
        return donorlist

    def getdonations(name):
        """function to get the donations for a given donor"""
        donations = donors[name]
        return donations

    def nameselect(name, donations):
        """function for updating the donations for a donor"""

        try:
            newdonation = int(utilities.safeinput('Please enter additional donation amount:\n'))
        except ValueError:
            utilities.clear()
            print('Input must be a number, please try again')
            utilities.safeinput('Press any key to continue...')
            utilities.clear()
            mailroom.nameselect(name, donations)

            # this helps prevent instantiating the rest of the code block if there is an exception
            return

        if newdonation < 0:
            print('Donation value cannot be negative')
            utilities.safeinput('')
            utilities.clear()
            mailroom.nameselect(name, donations)
        utilities.clear()
    
        donations.append(newdonation)
        donors.update({name: donations})
        total = sum(donations)
        mailroom.printemail(name, total)

    def printemail(name, total):
        """function for printing the thank you email for a donation"""
        print('Dear ' + name + ', \n')
        print('Thank you for you generous donations totalling $' + str(total) + '.\n')
        print('Because of kind donors such as yourself we will be able to continue to provide services for years to come.\n')
        print('Sincerely,')
        print('Derek Zoolander')
        print('Director, Center for Kids Who Can\'t Read Good And Wanna Learn to do Other Stuff Good Too')
        utilities.safeinput('')
        utilities.clear()
        return name, total

    def printreport():
        """function for generating a donor report"""
        report_dict = {}

        print('Donor Name     | Total Given | Num Gifts | Average Gift')
        print('-------------------------------------------------------')
        for name in donors.keys():
           report_dict.update(mailroom.createdatadictionary(name))

        for name, values in sorted(report_dict.items(), key=operator.itemgetter(1), reverse=True):
            print("{:<16} ${:<12} {:<11} ${:<6}".format(name, values[0], values[1], values[2]))
        utilities.safeinput('')
        utilities.clear()
        mailroom.menu()

    def createdatadictionary(name):
        """function for creating the report dictionary"""
        data_dict = {}
        qty = len(donors[name])
        total = sum(donors[name])
        average = round(total/qty, 2)
        data_dict.update({name: [total, qty, average]})
        return data_dict
    
def main():
    """main function"""
    mailroom.menu()

if __name__ == '__main__':
    main()