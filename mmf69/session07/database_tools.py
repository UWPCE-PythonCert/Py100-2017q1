#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('donor.db')

print("Opened database successfully")


def drop_table():
    try:
        conn.execute("drop table if exists donors")
    except IOError as error:
        print(error)


def create_table():
    try:
        conn.execute('''CREATE TABLE DONORS
           (DONOR_ID INT     NOT NULL,
           DONOR_NAME           TEXT    NOT NULL,
           DONATION_AMOUNT         REAL);''')
        print("Table created successfully")
    except IOError as error:
        print(error)


def insert_data():
    try:
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
    except IOError as error:
        print(error)


def menu_options():
    """Make a function for the code that allows the user to Add or Remove tasks from the list,
    plus save the tasks in the List tasks-priorities using numbered choices."""
    print("""
        Please Select an option:
        1) Drop Table
        2) Create Table
        3) Insert Initial Data
        4) Exit Tool
        """)

