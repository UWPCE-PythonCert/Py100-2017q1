# Javier Vazquez
# Grid Printer
# Jan 31, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/list_lab.html

import os

def thanks(donors):
    flag = 0
    print("Type [list] to display donors list.")
    print("Type a name to look in donors list or add a new one.")
    name = input("Input: ")
    if name == "list":
        for donor in donors:
            print(donor[0])
    elif name not in [donor[0] for donor in donors if name in donor]:
        print("new donor")
    elif name in [donor[0] for donor in donors if name in donor]:
        print(name)

def report(donors):
    donors.sort(key = lambda x: x[1], reverse=True)
    print("{0:<20}{1:>13}{2:^20}{3:>25}".format("Name", "Total Donated", "No. of Donations", "Avg. of Donations"))
    for donor in donors:
        print("{0:<20}{1:>13}{2:^20}{3:>25.2f}".format(donor[0], donor[1], donor[2], donor[3]))


def main():
    donors = [["Maximus Decimus", 1000, 1, 1000/1], ["William Wallace", 2000, 2, 2000/2],
              ["Joan of Arc", 3500, 3, 3500/3], ["Bruce Wayne", 1000000, 1, 1000000/1]]
    report(donors)
    thanks(donors)


if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main()