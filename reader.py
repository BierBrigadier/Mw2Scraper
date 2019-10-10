import glob
import os


# Enumerate files in the log folder. Returns list of filenames
def enumFiles():
    file_list = glob.glob("log/localhost-28961/*.json")
    print("There are " + str(len(file_list)) + " logs found.")
    return file_list


# Read content of a file and close it. Return content as string
def ReadFile(filename):
    file_object = open(filename, "r")
    file_content = file_object.read()
    file_object.close()
    return file_content


# Compares two files. Return boolean.
def CompareFiles(file_a, file_b):
    if file_a == file_b:
        return True
    else:
        return False


def RemoveFile(file):
    if os.path.isfile(file):
        os.remove(file)
    else:
        print("Error: %s file not found" % file)


# Removes duplicate files and returns distinct list
def RemoveDuplicateFiles(file_list):
    duplicates = -1
    for i in range(len(file_list)):
        try:
            file_a = ReadFile(file_list[i])
            file_b = ReadFile(file_list[i + 1])
            # Check if their content is the same
            if (CompareFiles(file_a, file_b)):
                duplicates = duplicates + 1
                # Remove the file
                RemoveFile(file_list[i])
        except IndexError:
            pass
        continue
    if str(duplicates) != "-1":
        print("Removed: " + str(duplicates) + " duplicates")

print("Tool created by Justin.\n")
file_list = enumFiles()
RemoveDuplicateFiles(file_list)
file_list = enumFiles()
print("Reading files done.\n")
