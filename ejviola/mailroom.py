#!/usr/bin/env python3

# Create a list to hold lists of donations
donordata = []

# Start list with some sample donations
donordata.append(["Bill Gates", 3000000])
donordata.append(["Bill Gates", 1125000])
donordata.append(["Bill Gates",100125])
donordata.append(["Elon Musk", 1500000])
donordata.append(["Paul Allen", 2000000])
donordata.append(["Paul Allen", 134000])
donordata.append(["Mark Zuckerberg", 125000])
donordata.append(["Jeff Bezos", 1])

# While loop to let user send thank you notes or view a report
while True:
    choice = float(input("Choose one of the following (Enter 1, 2, or 3): \n 1) Send a Thank You \n 2) Create a Report \n 3) Quit\n"))

    # Create a list of unique donors
    donorlist = []
    for i in donordata:
        # row = str(donordata[i]).split(",").strip("[").strip("]")
        row = i[0]
        # If that donor is already in the list, do nothing
        if row in donorlist:
            counter = []
        # Otherwise, add that donor
        else:
            donorlist.append(row)
    if choice == 1:
        print("You chose: send a thank you\n")
        while True:
            # Ask the user to enter a name or type 'list'
            entername = str(input("Please enter the full name of the donor you would like to thank, \nenter 'list' to see a list of donors, \nor enter 'back' to go back to the main directory:\n"))
            # Construct the list of donors

            # If the user asks for a list of donors, print the list
            if entername.lower() == "list":
                print(donorlist)
                print("\n")
                break
            elif entername.lower() == "back":
                break
            else:
                if entername in donorlist:
                    print("You selected "+entername+"\n")
                    try:
                        amount = float(input("How much did "+entername+" donate?\n"))
                    except:
                        print("Error: not a valid amount \n")
                    donordata.append([entername, amount])

                else:
                    #add to list
                    donorlist.append(entername)
                    print(entername+" was not in the existing data. "+entername+" has been added to the list of donors.\n")
                    try:
                        amount = float(input("How much did "+entername+" donate?\n"))
                    except:
                        print("Error: not a valid amount \n")
                    donordata.append([entername, amount])
            # Print thank you
            print("Dear "+entername+",\n    I would like to take this opportunity to thank you for your generous donation of $"+str(amount)+". \nYour thoughtful contribution to our philanthropic efforts will help go towards important social missions,\nallowing us to leverage our areas of expertise to create positive, equitable outcomes for all involved. \n \nThank you for your support,\n    Eric Viola\n\n")

    elif choice == 2:
        print("You chose: create a report\n")

        # Count and sum donations
        donationsum = []
        donationcount = []
        for i in donorlist:
            localsum = 0
            localcount = 0
            for row in donordata:
                if i == row[0]:
                    localsum += row[1]
                    localcount += 1
            donationsum.append(localsum)
            donationcount.append(localcount)

        # Combine list of names, donation sums, and donation counts
        counter = 0
        report = []
        for i in donorlist:
            newrow = [donationsum[counter], donorlist[counter],donationsum[counter], donationcount[counter], donationsum[counter] / donationcount[counter]]
            report.append(newrow)
            counter += 1

        # Write a report, sorted by donationsum
        report = sorted(report, reverse=True)
        print("Name:  \t\t\t\t\t\tTotal Donated: Donations:\tAverage Donations:\n")
        for i in report:
            name = i[1]+(27-len(i[1]))*" "
            total = " $"+(13-len(str(i[2])))*" "+str(i[2])
            count = (11-len(str(i[3])))*" "+str(i[3])
            average = "   $"+(17-len(str(i[4])))*" "+str(i[4])
            print(name+total+count+average)
        print("\n")

    elif choice == 3:
        break
    else:
        print("Please enter 1, 2, or 3")