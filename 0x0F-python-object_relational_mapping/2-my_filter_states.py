#!/usr/bin/env python3
"""Script that displays all values in the states table of hbtn_0e_0_usa where
   name matches a given argument."""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <MySQL username> <MySQL password> "
              "<database name> <state name searched>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    # Connect to the MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=database,
                         port=3306, host='localhost', charset="utf8")

    # Create a cursor object
    cursor = db.cursor()

    # Build and execute the SQL query
    query = ("SELECT * FROM states WHERE name LIKE BINARY %s "
             "ORDER BY states.id ASC")
    cursor.execute(query, (state_name,))

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
