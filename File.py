# File class to deal with loading and parsing through a file

DELIMITER = "|~|"


class File:
    fileName = None
    filePointer = None

    def __init__(self, file):
        self.fileName = file

    def loadFile(self):
        try:
            f = open(self.fileName, "r")
        except IOError:  # if file doesn't exist, create one
            f = open(self.fileName, 'w')
        self.filePointer = f

    def extractUserName(self):  # Takes in file
        # Load name
        try:
            name = self.filePointer.readline().strip()
        except IOError:
            name = ""

        if not name:
            print("Hi! It seems that you're a new user. Welcome!")
            name = input("What is your name? ")
            self.filePointer.write("{}\n".format(name))
        else:
            print("Hi {}! Welcome back!".format(name))

        return name

    def loadUserData(self):
        try:
            lines = self.filePointer.readlines()
        except IOError:
            return []
        # Load data if any
        # data order: 0: weight, 1: note, 2: date and time
        count = 1
        data = []

        for line in lines:
            # print("Entry {}: Weight: {}, Note: {}, Date: {}".format(
            #     count, entry[0], entry[1], entry[2]))

            data.append(self.combineData(line))
            count += 1

        return data

    def separateLines(self, line):
        entry = line.split(DELIMITER)
        return entry

    def combineData(self, line):
        parsedData = " | ".join(self.separateLines(line))
        return parsedData

    def addData(self, data):
        # Saving it to a textfile
        with open(self.fileName, "a") as f:  # in append mode
            f.write(data)

    def extractCols(self, user):
        weights = []
        notes = []
        dates = []

        with open(self.fileName) as f:
            lines = f.readlines()[1:]

        for line in lines:
            entry = self.separateLines(line)
            weights.append(entry[0])
            notes.append(entry[1])
            dates.append(entry[2].strip('\n'))

        user.setWeights(weights)
        user.setNotes(notes)
        user.setDates(dates)

        f.close()
