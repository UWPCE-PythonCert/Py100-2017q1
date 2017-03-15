#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('donor.db')

conn.execute("drop table if exists donors")