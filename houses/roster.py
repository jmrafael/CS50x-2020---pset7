from sys import argv, exit
import csv
from cs50 import SQL

if len(argv) == 2:

    # Open the file for SQLite
    db = SQL("sqlite:///students.db")

    # Getting data
    allData = db.execute("SELECT DISTINCT first, middle, last, birth FROM students WHERE house = (?) ORDER BY last, first", argv[1])

    # Iterate the the query and print the result
    for row in allData:
        if row["middle"] != None:
            middle = row["middle"].strip()
            print(row["first"] + " " + middle + " " + row["last"] + ", born " + str(row["birth"]))
        else:
            print(row["first"] + " " + row["last"] + ", born " + str(row["birth"]))

else:
    print("Usage: python roster.py House")
    exit(1)