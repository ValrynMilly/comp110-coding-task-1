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
c.execute("INSERT INTO numbers VALUES (98102, 'MILLY!')")
c.execute("INSERT INTO numbers VALUES (95432, 'LAURA!')")
c.execute("INSERT INTO numbers VALUES (82082, 'BEAST!')")
c.execute("INSERT INTO numbers VALUES (71923, 'BRIAN!')")
c.execute("INSERT INTO numbers VALUES (60203, 'AARON!')")
c.execute("INSERT INTO numbers VALUES (59287, 'BURRY!')")
c.execute("INSERT INTO numbers VALUES (50412, 'BLUEG!')")
c.execute("INSERT INTO numbers VALUES (20495, 'EXCEL!')")
c.execute("INSERT INTO numbers VALUES (19999, 'JAMES!')")
c.execute("INSERT INTO numbers VALUES (14030, 'STEVE!')")
c.execute("TRUNCATE TABLE numbers")

conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM numbers")
print([(r[0], r[1]) for r in c.fetchall()])

