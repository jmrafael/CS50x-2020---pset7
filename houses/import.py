import csv
from sys import argv, exit
from cs50 import SQL

# Check the length of arguments
if len(argv) == 2 and argv[1].endswith('.csv'):

    # Open the file for SQLite
    db = SQL("sqlite:///students.db")

    #Open file
    file = open(argv[1], 'r')
    reader = csv.DictReader(file)

    #iterate the file
    for row in reader:
        names = row["name"]
        AllNames = names.split()

        #Inserting in first and last name cenarious
        if len(AllNames) == 2:
            fName = AllNames[0]
            lName = AllNames[1]
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", fName, None, lName, row["house"], row["birth"])
        #Inserting in first, middle and last name cenarious
        if len(AllNames) == 3:
            fName = AllNames[0]
            mName = AllNames[1]
            lName = AllNames[2]
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", fName, mName, lName, row["house"], row["birth"])
else:
    print("Usage: python import.py characters.csv")
    exit(1)