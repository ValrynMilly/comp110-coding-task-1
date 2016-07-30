#!/usr/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='surferdb',
    user='root',
    passwd='Enthusiast123',
    host='127.0.0.1')
c = conn.cursor()


# Print the contents of the database.
c.execute("SELECT * FROM numbers ORDER BY score LIMIT 10")
print([(r[0], r[1]) for r in c.fetchall()])
