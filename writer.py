import os

blacklistedlines = []


def openWriteFile():
    database = open('database/database.txt', 'a')
    return database


def writeToFile(line, database):
    database.write(line)


def closeWriteFile(database):
    database.close()


def removeFile(file_name):
    os.remove(file_name)


def removeDuplicates():
    print("Cleaning up file...")
    lines_seen = set()  # holds lines already seen
    outfile = open('database/databasetemp.txt', "w")
    for line in open('database/database.txt', "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    os.remove('database/database.txt')
    os.rename('database/databasetemp.txt', 'database/database.txt')
    print("Cleaning up done.\n")
