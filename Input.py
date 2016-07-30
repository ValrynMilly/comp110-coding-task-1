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

# Insert some example data.
c.execute("INSERT INTO numbers VALUES (11, 'Thrbcvee!')")

conn.commit()

