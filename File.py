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

            data.append(self.separateLines(line))
            count += 1

        return data

    def separateLines(self, line):
        entry = line.split(DELIMITER)
        parsedData = " | ".join(entry)
        return parsedData

    def addData(self, data):
        # Saving it to a textfile
        with open(self.fileName, "a") as f:  # in append mode
            f.write(data)
