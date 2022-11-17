f1 = str(input("Enter the name of the first input file: "))
f2 = str(input("Enter the name of the second input file: "))
outputFile = open("fileAnalysis.txt", "w")


#  * Functions to interpret files  *   #
# Parse separates the words entered by new line, and returns the data split by space


def Parse(x):
    with open(x) as data_file:
        data = []
        for line in data_file:
            data = data + line.split()
        return data
        #for space in line_data:
        #    data = space.split()
         #   return data


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
        if item not in z:  # if item does not already exist in z, item is appended to array
            z.append(item)
    for item in y:
        if item not in z:  # if item does not already exist in z prior to scan for array x, item is appended to array
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
        if item in y:  # if item already existed in the frequency table, continue with the next item in loop
            continue
        for item2 in x: # for each item in the array passed in function
            if item == item2:  # if item matches item 2,
                y[item] = count  # add that item into the array with the initial count 1 (if passed first time)
                count = count + 1  # add to subsequent counts of that word
    title = str("{:<20} {:<15}".format('Word', 'Count') + "\n")  # {:<(integer)} are padding formatting codes. "<"
    #  signifies to pad right
    table = ""
    for word, value in y.items():  # word = key, value = count of word/value of key-value pair
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
