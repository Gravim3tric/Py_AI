import sqlite3
import csv

def databaseSSH():
    CVS_ENTRYDICT = {} #ENTRIES FROM THE CVS FILE
    USED_IPS = [] #IPS THAT ARE IN THE DATABASE FILE
    x = 1

    try:
        with open("data/sshlist.csv") as csvfile: #Reading Cvs File for SSH Information
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                if "IP" in row:
                    continue
                IP = row[0]
                USERNAME = row[1]
                PASSWORD = row[2]
                if x not in CVS_ENTRYDICT: #Stores SSH information in a list in a dictionary
                    d = {x:[IP,USERNAME,PASSWORD]}
                    CVS_ENTRYDICT.update(d)
                    print(row[0])
                    print(row[1])
                    print(row[2])
                    x+=1
                elif x in CVS_ENTRYDICT:
                    x+=1
                    continue

    except Exception as e: #Error if there is no CSV FILE
        print(e)
        print("ERROR, COULD NOT FIND CSV")
        return

    db = sqlite3.connect('data/sshdb') #Creates or modifies the Database file "sshdb"
    cursor = db.cursor()

    try:
        cursor.execute("""
            CREATE TABLE sshlist(IP TEXT, USERNAME TEXT, PASSWORD TEXT)
        """) #Creates Table if not already there
        db.commit()

    except sqlite3.OperationalError as e:
        print(e)
        None

    cursor.execute('''SELECT * FROM sshlist''') #Reads from the "sshlist" table if not already existing
    all_rows = cursor.fetchall()
    if all_rows: #If there is information in the tables, it takes the IP of each row and adds it to the USED IP list
        for each in all_rows:
            USED_IPS.append(each[0])

    for each in CVS_ENTRYDICT.values(): #Checks to see if the IPS in CSV File are in the DB, if so, skips over it and commits to DB
        if each[0] in USED_IPS:
            continue
        else:
            cursor.execute("""
                INSERT INTO sshlist(IP,USERNAME,PASSWORD)
                VALUES(?,?,?)""", (each[0],each[1],each[2]))
            db.commit()
    x = 1
    Returned_Dict= {}
    cursor.execute("""SELECT * FROM sshlist""")
    all_rows=cursor.fetchall()
    for each in all_rows:
        d = {str(x):each}
        Returned_Dict.update(d)
        x+=1
    return Returned_Dict
