from Weight import Weight
from Graph import Graph
from User import User
from File import File


class Interface:
    running = None
    choice = ""
    user = None
    file = None

    def startInterface(self):
        self.running = True

    def loadInformation(self, fileName):
        self.user = User()
        self.file = File(fileName)

        self.file.loadFile()
        self.user.setUserName(self.file.extractUserName())
        self.user.setData(self.file.loadUserData())

        self.file.extractCols(self.user)

    def userChoices(self):
        print("1. Add entry")
        print("2. Look at all entry")
        print("3. Check out graph")
        print("4. Analysis of data")
        print("5. Quit")

    def askForUserChoice(self):
        self.choice = input("What would you like to do? (number input) ")

    def addWeight(self):
        # To do: make this into a function part of the class
        weight = input("What was your recorded weight? ")
        note = input("Any Note? ")
        print("Adding entry...")
        weight = Weight(weight, note)

        # confirmation
        print("You just recorded {} pounds and your note is: '{}' on {} at {}".format(
            weight.getWeight(), weight.getNote(), weight.getTime().strftime("%m/%d/%Y"), weight.getTime().strftime("%H:%M")))

        self.file.addData(weight.toString())

        self.user.addData(self.file.separateLines(
            weight.toString()))
        print("Entry saved\n")

    def showData(self):
        count = 1
        for entry in self.user.getData():
            print("{}: {}".format(count, entry))
            count += 1

    def showGraph(self):
        graph = Graph()
        graph.simpleGraph(self.user.getDates(), self.user.getWeights())
        # print("Sorry, this feature has not been implemented yet.\n")

    def showAnalysis(self):
        pass

    def setRunningFalse(self):
        self.running = False
        print("Quitting...\n")

    def checkUserChoice(self):
        print("---------------------\n")
        if self.choice == "1":
            self.addWeight()
        elif self.choice == "2":
            self.showData()
        elif self.choice == "3":
            self.showGraph()
        elif self.choice == "4":
            self.showAnalysis()
        elif self.choice == "5":
            self.setRunningFalse()
        else:
            print("Invalid number choice, please choose a valid number choice")
        print("---------------------")
