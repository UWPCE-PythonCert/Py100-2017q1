donors = [
            {"Name":"Donor", "Amount":"Total Donated", "Number":"Number of Donations"},
            {"Name":"Gregory Blazek", "Amount":30, "Number":1},
            {"Name":"Tiffany Huntley", "Amount":1070, "Number":2},
            {"Name":"Gabriel Mora", "Amount":2050, "Number":3},
            {"Name":"Courtney Barrett", "Amount":765, "Number":2},
            {"Name":"Andrew Noodle", "Amount":2098, "Number":3}
]
individualDonations = [
    {"Name":"Gregory Blazek","Amount":30},
    {"Name":"Tiffany Huntley","Amount":1000},
    {"Name":"Tiffany Huntley","Amount":70},
    {"Name":"Gabriel Mora","Amount":1000},
    {"Name":"Gabriel Mora","Amount":1000},
    {"Name":"Gabriel Mora","Amount":50},
    {"Name":"Courtney Barrett","Amount":750},
    {"Name":"Courtney Barrett","Amount":15},
    {"Name":"Andrew Noodle","Amount":1000},
    {"Name":"Andrew Noodle","Amount":1000},
    {"Name":"Andrew Noodle","Amount":98}

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
    if thanksChoice.lower()=='list':
        listName = []
        for donor in donors:
            listName.append(donor["Name"])
        print(listName)
    else:
        for donor in donors:
            if thanksChoice in donor["Name"]:
                thanksDonation = int(input(("Enter " + thanksChoice + "'s donation amount: ")))
                donor["Amount"] += thanksDonation
                donor["Number"] += 1
                print("\nThe following was was emailed to " + thanksChoice + ":\n")
                print("Dear " + thanksChoice + ",\nThank you for your kind donation of " + str(thanksDonation) + " dollars.\n")
                indDonation = {"Name":thanksChoice,"Amount":thanksDonation}
                individualDonations.append(indDonation)
                break


        else:
            newDonor = {"Name":None, "Amount":None, "Number":0}
            print(thanksChoice + " was not found. Added " + thanksChoice + " to donors list")
            thanksDonation = int(input(("Enter " + thanksChoice + "'s donation amount: ")))
            print("\nThe following was was emailed to " + thanksChoice + ":\n")
            print("Dear " + thanksChoice + ",\nThank you for your kind donation of " + str(
                thanksDonation) + " dollars.\n")
            newDonor["Name"], newDonor["Amount"], newDonor["Number"] = thanksChoice, thanksDonation, newDonor["Number"] + 1
            donors.append(newDonor)
            indDonation = {"Name": thanksChoice, "Amount": thanksDonation}
            individualDonations.append(indDonation)


def createReport():
    widths = 20
    for donor in donors:
        total = str(donor["Amount"])
        number = str(donor["Number"])
        print(donor["Name"].ljust(widths) + total.ljust(widths) + number.ljust(widths))
    print("")
def reportIndividual():
    print(individualDonations)

while(True):
    menuChoice = showMenu()
    if menuChoice == "1" or menuChoice == "send a thank you":
        sendThanks()
    elif menuChoice == "2" or menuChoice == "create a report":
        report = input("Choose \'Individual Donations(1)\' or \'Total Donations(2)\'")
        if report == "1" or report.lower()=="individual donations":
            reportIndividual()
        if report == "2" or report.lower() == "total donations":
            createReport()
    elif menuChoice == "3" or menuChoice == "quit":
        input("Press enter to confirm exit")
        break