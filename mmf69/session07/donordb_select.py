#!/usr/bin/python

from prettytable import PrettyTable
import sqlite3


conn = sqlite3.connect('donor.db')
print("Opened database successfully")

cursor = conn.execute("SELECT DONOR_ID,DONOR_NAME,DONATION_AMOUNT from DONORS")
for row in cursor:
    print(row)


cursor = conn.execute("SELECT DONOR_ID,DONOR_NAME,total(DONATION_AMOUNT),"
                      "count(distinct DONATION_AMOUNT),total(DONATION_AMOUNT)/count(distinct DONATION_AMOUNT)"
                      " from donors group by DONOR_ID,DONOR_NAME")
for row in cursor:
    print("DONOR_ID = ", row[0])
    print("DONOR_NAME = ", row[1])
    print("TOTAL_DONATIONS = ", row[3])
    print("DONATION_AMOUNT = ", row[2])
    print("AVERAGE_DONATION = ", row[4], "\n")


print("*********************************DONOR REPORT***************************************")

cursor = conn.execute("SELECT DONOR_ID as 'Donor ID',DONOR_NAME as 'Donor Name',"
                      "total(DONATION_AMOUNT) AS 'Total Donations',"
                      "count(DONOR_ID) AS 'Number of Donations',"
                      "total(DONATION_AMOUNT)/count(DONOR_ID) AS AVERAGE_DONATION"
                      " from donors group by DONOR_ID,DONOR_NAME")

col_names = [cn[0] for cn in cursor.description]
rows = cursor.fetchall()

x = PrettyTable(col_names)
x.align[col_names[1]] = "l"
x.align[col_names[2]] = "r"
x.padding_width = 1
for row in rows:
    x.add_row(row)

print(x)


print("Operation done successfully")

conn.close()
