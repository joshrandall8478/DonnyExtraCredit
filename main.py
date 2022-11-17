#f1 = str(input("Enter the name of the first input file: "))
#f2 = str(input("Enter the name of the second input file: "))
f1 = str("file1.txt")

# uniqueF1 =
# uniqueF2 =
# union =
# intersection =
# exclusiveF1 =
# exclusiveF2 =
# frequencyF1 = {}
# frequencyF2 = {}

def parse(x):
    with open(x) as data_file:
        for space in data_file:
            data = space.split()
            return data


def removeDuplicates(x):
    y = []
    for item in x:
        for item2 in x:
            if x.index(item) != x.index(item2):
                if item == item2:
                    x.remove(item2)
    return y


uniqueF1 = removeDuplicates(parse(f1))
#uniqueF2 = parse(f2)
print(uniqueF1)
# def unique(x):
