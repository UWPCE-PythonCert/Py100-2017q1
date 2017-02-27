#!/usr/bin/env python3
import pickle


# class Donor loads donor db, can add donor or delete donor, and saves the db, print donor information
class Donor (object):

    def __init__(self):
        donor_db={}

    def load_donordb(self):
        try:
            with open('mailroom.pickle', 'rb') as db_handle:
                donor_db = pickle.load(db_handle)
        except IOError:
            donor_db = {
                "Tevin Campbell": ("Male",59),
                "Captain Tennille": ("Male",79),
                "Irene Cara": ("Female",34),
                "Barry Carl": ("Female",27),
                "Brandi Carlile":("Male",44)
            }
        return donor_db

    def save_donordb(self,db):
        try:
            with open('mailroom.pickle', 'wb') as db_handle:
                pickle.dump(db, db_handle)
        except IOError:
            raise "Error: Unable to save donor database."

    def add_donor(self,db,donor,gender,age):
        if donor in db.keys():
            db[donor].append(gender,float(age))
        else:
            db[donor] = (gender,float(age))
        return db

    def delete_donor(self,db,donor):
        if donor in db.keys():
            del db[donor]
        else:
            print("{} does not exist.".format(donor))
        return db

    def print_donors(self,db):
        for key,value in db.items():
            print ("donor name: {}, donor attribute{}".format(key,value))

# class donation has donation details, it can add donation amount, load donation db and save donation db, print donation summary
class Donation (object):

    def __init__(self):
        donation={}

    def load_donationdb(self):
        try:
            with open('mailroomdonation.pickle', 'rb') as db_handle:
                    donation_db = pickle.load(db_handle)
        except IOError:
            donation_db = {
                "Tevin Campbell": [988,7876,50],
                "Captain Tennille": [580],
                "Irene Cara": [780,340,550],
                "Barry Carl": [230,456,900],
                "Brandi Carlile":[780]
            }
        return donation_db

    def save_donationdb(self,db):
        try:
            with open('mailroomdonation.pickle', 'wb') as db_handle:
                pickle.dump(db, db_handle)
        except IOError:
            raise "Error: Unable to save donor database."

    def add_donation(self,db,donor,amount):
        if donor in db.keys():
            db[donor].append(float(amount))
        else:
            db[donor] = [float(amount)]
        return db

    def print_summary_report (self,db):
        for key in db:
            s=sum(db[key])
            c=len(db[key])
            a=float(s/c)
            print("donor name: {}, total_donation_amount: {}, average_donation_amount:{:.2f}".format(key,s,a))



if __name__ == "__main__":
    while True: #while loop if input value not in the defined value, it just go back to the first input.
        user_prompt=input("1.Show me all the donors; 2.Show me donation report; 3.quit > ")
        if user_prompt not in '1234':
            print("Please select a number that is in the range of 1 to 4.")

        if user_prompt=="1":
            donor=Donor()
            donordb=donor.load_donordb()
            donor.save_donordb(donordb)
            donor.print_donors(donordb)

        if user_prompt=="2":
            donation=Donation()
            donationdb=donation.load_donationdb()
            donation.save_donationdb(donationdb)
            donation.print_summary_report(donationdb)

        if user_prompt=="3":
            print("goodbye")
            break




