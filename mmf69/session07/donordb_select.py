#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('donor.db')
print("Opened database successfully")

cursor = conn.execute("SELECT DONOR_ID,DONOR_NAME,DONATION_AMOUNT  from DONORS")
for row in cursor:
   print("DONOR_ID = ", row[0])
   print("DONOR_NAME = ", row[1])
   print("DONATION_AMOUNT = ", row[2], "\n")

print("Operation done successfully")
conn.close()