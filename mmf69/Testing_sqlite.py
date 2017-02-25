#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('donor.db')

print("Opened database successfully")

#  conn.execute("drop table if exists donors")

conn.execute('''CREATE TABLE DONORS
       (ID INT PRIMARY KEY     NOT NULL,
       DONOR_NAME           TEXT    NOT NULL,
       DONATION_AMOUNT         REAL
       UPDATE_DATE_TIME DATETIME DEFAULT CURRENT_TIMESTAMP);''')
print("Table created successfully")

conn.close()
