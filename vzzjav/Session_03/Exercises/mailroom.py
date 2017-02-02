# Javier Vazquez
# Grid Printer
# Jan 31, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/list_lab.html

import os

def donation(donors):
    donation = 0
    print("Type [list] to display donors list.")
    print("Type a name to look in donors list or add a new one.")
    name = input("Input: ")
    if name == "list":
        for donor in donors:
            print(donor[0])
        return donors
    elif name not in [donor[0] for donor in donors if name in donor]:
        print("New donor: ", name)
        while True:
            try:
                donation = int(input("Donation: "))
                break
            except ValueError:
                print("Please provide a numeric value!")
        donors.append([name, donation, 1, donation/1])
        thanks(len(donors) - 1, donation, donors)
        return donors
    elif name in [donor[0] for donor in donors if name in donor]:
        print("Donor: ", name)
        while True:
            try:
                donation = int(input("Donation: "))
                break
            except ValueError:
                print("Please provide a numeric value!")
        index = [i for i in range(len(donors)) if name in donors[i][0]]
        index = index[0]
        donors[index][1] += donation
        donors[index][2] += 1
        donors[index][3] = donors[index][1]/donors[index][2]
        thanks(index, donation, donors)
        return donors

def thanks(index, donation, donors):
    print('''{0},

    On behalf of XYZ Organization, I would like to thank you
    for your contribution of ${1}. Your financial support helps
    us continue in our mission and the assist those in our community.

    The generous support of individuals like you makes it possible
    for our organization to exist and to make the community a great
    place to live.

    Thank you again for your support!

    Sincerely,
    XYZ Organization\n'''.format(donors[index][0], donation))


def report(donors):
    donors.sort(key = lambda x: x[1], reverse=True)
    print("{0:<20}{1:>13}{2:^20}{3:>25}".format("Name", "Total Donated", "No. of Donations", "Avg. of Donations"))
    for donor in donors:
        print("{0:<20}{1:>13}{2:^20}{3:>25.2f}".format(donor[0], donor[1], donor[2], donor[3]))


def main():
    donors = [["Maximus Decimus", 1000, 1, 1000/1], ["William Wallace", 2000, 2, 2000/2],
              ["Joan of Arc", 3500, 3, 3500/3], ["Bruce Wayne", 1000000, 1, 1000000/1]]
    report(donors)
    while True:
        donors = donation(donors)
        if input("Type [quit] to quit.") == "quit":
            break
        report(donors)


if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main()