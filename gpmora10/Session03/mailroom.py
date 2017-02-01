donors = [
    ["Donor", "Total Donated", "Number of Donations"],
    ["Gregory Blazek", 30, 1],
    ["Tiffany Huntley", 1070, 2],
    ["Gabriel Mora", 2050, 3],
    ["Courtney Barrett", 765, 2],
    ["Andrew Noodle", 2098, 3]
]

def showMenu():
    usrchoice = input("Please choose an option:\n"
          "1. Send a Thank You\n"
          "2. Create a Report\n"
          "3. quit\n"
          "Type in the option or the number: ")
    return usrchoice.lower()

def sendThanks():
    thanksChoice = input("Enter a donor's name or enter \"list\" to see a list of donors: ")
   #if thanksChoice in [name for donor in donors for name in donor]:
    for donor in donors:
        if thanksChoice in donor:
            thanksDonation = int(input(("Enter " + thanksChoice + "'s donation amount: ")))
            donor[1] += thanksDonation
            donor[2] += 1
            print("The following was was emailed to " + thanksChoice + ":\n")
            print("Dear " + thanksChoice + ",\nThank you for your kind donation of " + str(thanksDonation) + " dollars.\n")
            break

    else:
        newDonor = [None, None, 0]
        print(thanksChoice + " was not found. Added " + thanksChoice + " to donors list")
        thanksDonation = int(input(("Enter " + thanksChoice + "'s donation amount: ")))
        print("The following was was emailed to " + thanksChoice + ":\n")
        print("Dear " + thanksChoice + ",\nThank you for your kind donation of " + str(
            thanksDonation) + " dollars.\n")
        newDonor[0], newDonor[1], newDonor[2] = thanksChoice, thanksDonation, newDonor[2] + 1
        donors.append(newDonor)

def createReport():
    widths = 20
    for donor, total, number in donors:
        total = str(total)
        number = str(number)
        print(donor.ljust(widths) + total.ljust(widths) + number.ljust(widths))
    print("")

while(True):
    menuChoice = showMenu()
    if menuChoice == "1" or menuChoice == "send a thank you":
        sendThanks()
    elif menuChoice == "2" or menuChoice == "create a report":
        createReport()
    elif menuChoice == "3" or menuChoice == "quit":
        input("Press enter to confirm exit")
        break