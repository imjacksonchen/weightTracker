# File class to deal with loading and parsing through a file

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
            self.filePointer.readline()
        except IOError:
            return None
        # Load data if any
        # data order: 0: weight, 1: note, 2: date and time
        lines = self.filePointer.readlines()
        print(lines)
        count = 1
        data = []

        for line in lines:
            print(line)
            # Change delimter because this can easily be broken
            data = line.split("|~|")
            parsedData = " | ".join(data)
            print("Entry {}: Weight: {}, Note: {}, Date: {}".format(
                count, data[0], data[1], data[2]))
            data.append(parsedData)
            count += 1

        return data

    def addData(self, data):
        # Saving it to a textfile
        with open(self.fileName, "a") as f:  # in append mode
            f.write("{}\n".format(data))
