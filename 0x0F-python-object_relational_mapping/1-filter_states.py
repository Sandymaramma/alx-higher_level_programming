#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

# create a cursor object
    cur = db.cursor()

# execute SQL query
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")

# fetch results and print them
    rows = cur.fetchall()
    for row in rows:
        print(row)

# close cursor and database connection
    cur.close()
    db.close()
