#!/usr/bin/env python3

import os
import operator

#build our initial dictionary
donors = {
    'Ricky': [1000],
    'Bobby': [1100, 2200],
    'Hansel': [5000, 6000, 7000],
    'Mr. Burgandy': [1, 2, 3, 4],
    'Austin': [123, 4567, 78, 99, 100],
    'Dale': [14, 234, 878, 345, 345, 234],
}

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
        clear()
        main()

# build a menu for use
def menu():
    print('Please make a selection from the menu items below\n')
    print('1.  Send a Thank You Note\n')
    print('2.  Create a report\n')
    print('Press "q" to quit\n')
    selection = safeinput('')
    if selection == '1':
        clear()
        names()
    elif selection == '2':
        clear()
        printreport()
    elif selection == 'q':
        print('exiting...')
        exit(0)

def names():
    """function for looking up/listing/adding new donors"""
    name = safeinput('Please enter a name, or type "list" to view a list of available names (case sensitive):\n')
    clear()
    # if the name exists in our dictionary, use it
    if name in donors.keys():
        donations = donors[name]
        nameselect(name, donations)
    # you want a list of names? you got it
    elif name == 'list':
        clear()
        for key in donors.keys():
            print(key)
        print('')
        input('Press Enter to Continue...')
        clear()
        names()
    # you can't have a blank name silly
    elif name == '':
        clear()
        names()
    #add the new person to the dictionary
    else:
        newname = {name: []}
        donors.update(newname)
        donations = donors[name]
        nameselect(name, donations)

def nameselect(name, donations):
    """funcation for updating the donations for a donor"""

    newdonation = int(safeinput('Please enter additional donation amount:\n'))
    if newdonation < 0:
        print('Donation value cannot be negative')
        safeinput('')
        clear()
        nameselect(name,donations)
    clear()
    donations.append(newdonation)
    donors.update({name: donations})
    total = sum(donations)
    printemail(name, total)

def printemail(name, total):
    """function for printing the thank you email for a donation"""
    print('Dear ' + name +',\n')
    print('Thank you for you generous donations totalling $' + str(total) + '.\n')
    print('Because of kind donors such as yourself we will be able to continue to provide services for years to come.\n')
    print('Sincerely,')
    print('Derek Zoolander')
    print('Director, Center for Kids Who Can\'t Read Good And Wanna Learn to do Other Stuff Good Too')
    safeinput('')
    clear()
    menu()

def printreport():
    """function for generating a donor report"""
    report_dict = {}
    print('Donor Name     | Total Given | Num Gifts | Average Gift')
    print('-------------------------------------------------------')
    for name, donations in donors.items():
        qty = len(donations)
        total = sum(donations)
        average = round(total/qty, 2)
        report_dict.update({name: [total, qty, average]})

    for name, values in sorted(report_dict.items(), key=operator.itemgetter(1), reverse=True):
        print("{:<16} ${:<12} {:<11} ${:<6}".format(name, values[0], values[1], values[2]))
    safeinput('')
    clear()
    menu()

def main():
    menu()

if __name__ == '__main__':
    main()