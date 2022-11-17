import os.path

f1 = str(input("Enter the name of the first input file: "))

# Checks if the input file exists
if not os.path.isfile(f1):
    print("Please input a valid file name")
    exit()

f2 = str(input("Enter the name of the second input file: "))

if not os.path.isfile(f2):
    print("Please input a valid file name")
    exit()

# Checks if the output file already existed prior to the code being ran
if not os.path.isfile("fileAnalysis.txt"):
    outputFile = open("fileAnalysis.txt", "x")
else:
    outputFile = open("fileAnalysis.txt", "w")


#  * Functions to interpret files  *   #
# Parse separates the words entered by space, and returns the data split by space


def Parse(x):
    with open(x) as data_file:
        for space in data_file:
            data = space.split()
            return data


# RemoveDuplicates creates a new array, and only adds items that have not been added before to that array
# to remove said duplicates


def RemoveDuplicates(x):
    y = []
    for item in x:
        if item not in y:
            y.append(item)
    return y


# Unison combines two arrays into one

def Unison(x, y):
    z = []
    for item in x:
        if item not in z:
            z.append(item)
    for item in y:
        if item not in z:
            z.append(item)
    return z


# Intersection looks for values in x and only adds them into z if they are existing values in y, creating an
# intersection effect.


def Intersection(x, y):
    z = [value for value in x if value in y]
    return z


# Exclusive looks for values in x, and only adds them into z if they do not exist in y.


def Exclusive(x, y):
    z = [value for value in x if value not in y]
    return z


# FrequencyTable


def FrequencyTable(x):
    y = {}
    for item in x:
        count = 1
        if item in y:
            continue
        for item2 in x:
            if item == item2:
                y[item] = count
                count = count + 1
    title = str("{:<20} {:<15}".format('Word', 'Count') + "\n")
    table = ""
    for word, value in y.items():
        table = table + str("{:<20} {:<15}".format(word, value) + "\n")

    return title + table


# ArrayToString converts array values into readable strings for the files output.


def ArrayToString(x):
    y = ""
    for item in x:
        y = y + item + " "
    return y


# uniqueF1 and uniqueF2 are variables that chain RemoveDuplicates and Parse, so that we instantly have our
# unique words to use for the rest of the file output
uniqueF1 = RemoveDuplicates(Parse(f1))
uniqueF2 = RemoveDuplicates(Parse(f2))

# File outputs
outputFile.write("Unique words in file 1: " + ArrayToString(uniqueF1) + "\n")
outputFile.write("Unique words in file 2: " + ArrayToString(uniqueF2) + "\n")
outputFile.write("Unison of the words in file 1 and file 2: " + ArrayToString(Unison(uniqueF1, uniqueF2)) + "\n")
outputFile.write(
    "Intersection of the words in file 1 and file 2: " + ArrayToString(Intersection(uniqueF1, uniqueF2)) + "\n")
outputFile.write("words in file 1 but not in file 2: " + ArrayToString(Exclusive(uniqueF1, uniqueF2)) + "\n")
outputFile.write("words in file 2 but not in file 1: " + ArrayToString(Exclusive(uniqueF2, uniqueF1)) + "\n")
outputFile.write("words in file 1 but not in file 2 and words in file 2 but not in file 1: " + (
            ArrayToString(Exclusive(uniqueF1, uniqueF2)) + ArrayToString(Exclusive(uniqueF2, uniqueF1))) + "\n")
outputFile.write("frequency table for file 1:" + "\n")
outputFile.write(FrequencyTable(Parse(f1)) + "\n")
outputFile.write("frequency table for file 2:" + "\n")
outputFile.write(FrequencyTable(Parse(f2)) + "\n")

# Log to represent process success
outputFile.close()
print("data saved in fileAnalysis.txt")
