import reader
import writer
import re
import time




def ParsePlayer(ip, name, id, firstseen):
    current_player = name
    current_player += "\t" + id
    current_player += "\t" + ip
    current_player += "\t" + time.ctime(int(firstseen))
    return current_player


def ParseFile(file):
    content = reader.ReadFile(file)
    # Match: {ip":"XXXXXX","name"'
    regex_ip = '{"ip":"(.*?)","name"'
    stripped_ips = re.findall(regex_ip, content)

    # Match: "name":"XXXXXX","first
    regex_names = '"name":"(.*?)","first'
    stripped_names = re.findall(regex_names, content)

    # Match: "steamID":"XXXXXX","steamID_st
    regex_steamID = '"steamID":"(.*?)","steamID_str'
    stripped_steamIDs = re.findall(regex_steamID, content)
    for k in range(len(stripped_steamIDs)):
        stripped_steamIDs[k] = "http://steamcommunity.com/profiles/" + stripped_steamIDs[k]

    # Match: "firstSeen":XXXXXX,"steamID
    regex_firstSeen = '"firstSeen":(.*?),"steamID'
    stripped_firstSeen = re.findall(regex_firstSeen, content)

    # Parse all players from file:
    players_list = []
    for i in range(len(stripped_steamIDs)):
        retval = ParsePlayer(stripped_ips[i], stripped_names[i], stripped_steamIDs[i], stripped_firstSeen[i])
        players_list.append(retval)
    return players_list


# Parse all files using ParseFile(file):
def ParseFiles():
    print("Starting to parse and write...")
    file_list = reader.enumFiles()
    # Open database
    database = writer.openWriteFile()

    # For all files do:
    for i in range(len(file_list)):

        # For all lines in a file do:
        file = ParseFile(file_list[i])
        for k in range(len(file)):
            line = file[k]
            writer.writeToFile(line + "\n", database)
        writer.removeFile(file_list[i])
    # Close database
    writer.closeWriteFile(database)
    print("Parsing and writing done.")



while True:
    ParseFiles()
    writer.removeDuplicates()
    print("Thanks John van Boxtel for creating this tool!\n")
    time.sleep(60)
