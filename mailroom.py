#   $Id: play01.py,v 1.11 2017/02/12 20:27:25 larry Exp $

# Various import
# ---------------------------------------------------------------
import sys
import pickle
import os.path
import datetime
# ---------------------------------------------------------------

# Create dictionary
donors = {
"Bugs Bunny":[1000, 2000, 3000],
"Elmer Fudd":[500, 1200, 1600],
"Foghorn Leghorn":[800, 1600, 2400],
"Daffy Duck":[550, 750, 2400],
"Johnny Quest":[300, 600, 900],
"Marvin Martian":[5000, 10000, 20000],
"Porky Pig":[2500, 2800, 3000]}

# Open the pickle
try:
    # Open the pickle
    file_obj = open("/home/larry/UW/Play/donors", 'wb')

    # Put the donor dictionary in the pickle
    pickle.dump(donors, file_obj)

    # Close the pickle
    file_obj.close()

except:
    print("Could not open file, system exiting.")
    sys.exit()

# Open pickle for use, data looks like the following: name + donation amounts
# {'Bugs Bunny': [1000, 2000, 3000], etc.
donor_dict = pickle.load(open("donors", "rb"))

class menu_play:
    """
    Reads a pickle database into memory
    Dynamic menu
    Makes method choice based on user input
    """

    def __init__(self, msg = ["Placeholder"]):
        """
        Parameter is a list of from 1 to 9 strings
        """
        self.msg = msg

    def get_input(self):
        """
        User selects a routine
        """
        # Creates available choices list
        tst = [str(x) for x in range(1, len(self.msg) + 1)]

        # First element in menu choices
        v1 = tst[0]

        # Last element in menu choices
        v2 = tst[-1]

        # Show menu
        self.make_tui()

        # Insist on correct input & give feedback if wrong
        while True:
            chc = input()
            if not chc in tst:
                self.make_tui()
                print("You must enter a number from %s to %s." % (v1, v2))
            else:
                break

        # All available menu methods
        my_methods = {"1" : self.m1,
                      "2" : self.m2,
                      "3" : self.m3,
                      "4" : self.m4,
                      "5" : self.m5,
                      "6" : self.m6,
                      "7" : self.m7,
                      "8" : self.m8,
                      "9" : self.m9}

        # Call menu method based on user choice
        my_methods[chc]()

    def m1(self):
        """
        Add donor to database, check if name exists, give feedback to user
        """
        # Add donor if name is not existing in database
        while True:
            chc = input("Enter donor name to add: ")
            if chc in donors:
                print("Donor name %s already exists in database." % (chc))
            else:
                break

        donors[chc] = []
        print("%s added to donor database." % (chc))

    def m2(self):
        """
        Remove donor from database
        """
        # Remove donor if name exists in database
        while True:
            chc = input("Enter donor name to remove: ")
            if not chc in donors:
                print("Donor name %s does not exist in database." % (chc))
            else:
                break

        del donors[chc]
        print("%s removed from donor database." % (chc))

    def m3(self):
        """
        Find donor in database
        """
        # Get name of donor
        while True:
            chc = input("Enter donor name to report on: ")
            if not chc in donors:
                print("Donor name %s does not exist in database." % (chc))
            else:
                break

        # Donor name, number of donations, total & average donations
        num = str(len(donors[chc]))
        tot = sum(donors[chc])
        ave = float(sum(donors[chc]) / int(num))
        print("Name: %s ... Donations: %s ... Total: $%0.2f ... Average: $%0.2f." % (chc, num, tot, ave))

    def m4(self):
        """
        Add donation
        """
        # Name of donor
        while True:
            chc = input("Enter donor name to record donation to: ")
            if not chc in donors:
                print("Donor name %s does not exist in database." % (chc))
            else:
                break

        # Amount of donation
        new_don = 0
        while True:
            try:
                new_don = abs(float(input("Enter donation amount: ")))
            except ValueError:
                print("Not an number!")
                continue
            else:
                break

        # Add donation to dictionary value key
        donors[chc].append(new_don)

        # Alert user
        print("You have added $%.2f to %s's donation total." % (new_don, chc))

    def m5(self):
        """
        Report on selected donors
        """
        for x in donors:
            tot = sum(donors.get(x))
            num = len(donors.get(x))
            ave = float(tot) / num
            print("Name: %s ... Donations: %s ... Total: $%0.2f ... Average: $%0.2f." % (x, num, tot, ave))

    def m6(self):
        """
        Generate thank you letter
        """
        # Date and time
        tm = []
        today = datetime.date.today()
        tm.append(today)
        tm = tm[0]

        # Name of donor
        while True:
            chc = input("Enter donor name to record donation to: ")
            if not chc in donors:
                print("Donor name %s does not exist in database." % (chc))
            else:
                break

        # Donor total
        tot = sum(donors.get(chc))
                
        print("%s\n\nDear %s,\nThank you for your generous donation of $%0.2f.\n\nSincerely\n\nDonation committee" % (tm, chc, tot))

    def m7(self):
        """
        Ends mailroom routine
        """
        print("Mailroom ending")
        sys.exit()

    def m8(self):
        """
        Placeholder
        """
        pass

    def m9(self):
        """
        Placeholder
        """
        pass

    def make_tui(self):
        """
        Create simple TUI
        Maximum length of supplied string parameters is 50 characters.
        Maximum number of categories is 9
        Example | parameter = ["Report", "Thank you", "Quit"]
        +------------------------------+
        | Enter value and press RETURN |
        | [1] Report                   |
        | [2] Thank you                |
        | [3] Quit                     |
        +------------------------------+
        """

        # Check that supplied parameter is a valid list
        if len(self.msg) < 1 or len(self.msg) > 9:
            print("List must contain 1 to 9 strings")
            sys.exit()

        # Test string parameters in list
        for x in self.msg:
            if not type(x) is str or len(x) < 0 or len(x) > 50:
                print("List parameters must be strings between 0 & 50")
                sys.exit()

        hdr = "Enter value and press RETURN"
        hln = len(hdr)

        # Longest string in list
        ls = 0
        for x in self.msg:
            if len(x) > ls:
                ls = len(x)

        # Width of TUI
        if hln >= ls:
            spc = hln-3
        else:
            spc = ls + 1

        # Create interface
        cnt = 1

        print("\n+" + ("-" * (spc + 5)) + "+")
        print("| " + hdr + (((spc + 4) - len(hdr)) * " ") + "|")
        for x in self.msg:
            v1 = spc - len(x)
            print("| " + "[" + str(cnt) + "] " + x + v1 * " " + "|")
            cnt += 1
        print("+" + ("-" * (spc + 5)) + "+")

if __name__ == "__main__":
    lst = ["Add", "Remove", "Find", "Donation", "Report", "Thank you", "Quit"]
    mail_room = menu_play(lst)
    mail_room.get_input()
