#!/usr/bin/python

from prettytable import PrettyTable
import sqlite3

conn = sqlite3.connect('donor.db')
print("Opened database successfully")


def donor_list():
    print("********DONORS***********")
    cursor = conn.execute("SELECT DISTINCT DONOR_ID as 'Donor ID',"
                          "DONOR_NAME as 'Donor Name' from donors order by DONOR_ID")
    col_names = [cn[0] for cn in cursor.description]
    rows = cursor.fetchall()
    x = PrettyTable(col_names)
    x.align[col_names[0]] = "c"
    x.align[col_names[1]] = "l"
    x.padding_width = 1
    for row in rows:
        x.add_row(row)
    print(x)

donor_list()

print("Operation done successfully")

conn.close()
