#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('donor.db')
print("Opened database successfully")

conn.execute("INSERT INTO DONORS (DONOR_ID,DONOR_NAME,DONATION_AMOUNT) \
      VALUES (1, 'Sara', 100.00)")

conn.execute("INSERT INTO DONORS (DONOR_ID,DONOR_NAME,DONATION_AMOUNT) \
      VALUES (2, 'Starla', 50.00)")

conn.execute("INSERT INTO DONORS (DONOR_ID,DONOR_NAME,DONATION_AMOUNT) \
      VALUES (3, 'Tim', 100.00)")

conn.execute("INSERT INTO DONORS (DONOR_ID,DONOR_NAME,DONATION_AMOUNT) \
      VALUES (4, 'Ruby', 50.00)")

conn.execute("INSERT INTO DONORS (DONOR_ID,DONOR_NAME,DONATION_AMOUNT) \
      VALUES (4, 'Ruby', 25.00)")

conn.commit()
print("Records created successfully")
conn.close()