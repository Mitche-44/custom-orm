import sqlite3

# create a database connection
conn = sqlite3.connect("db/store.db")

# get a cursor object to execute sql queries
cursor = conn.cursor()

# print(help(cursor))
