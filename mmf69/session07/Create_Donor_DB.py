#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('donor.db')

print("Opened database successfully")

#  conn.execute("drop table if exists donors")


conn.execute('''CREATE TABLE DONORS
       (DONOR_ID INT     NOT NULL,
       DONOR_NAME           TEXT    NOT NULL,
       DONATION_AMOUNT         REAL);''')
print("Table created successfully")

conn.close()
