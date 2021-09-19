from Weight import Weight
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

    def userChoices(self):
        print("1. Add entry")
        print("2. Look at all entry")
        print("3. Check out graph")
        print("4. Quit")

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

        self.file.addData(weight)

        self.user.addData(weight)  # need to be changed
        print("Entry saved")

    def showData(self):
        # count = 1
        # for entry in self.user.getData():
        #     print("{}: {}".format(count, entry))
        #     count += 1
        print(self.user.getData())

    def showGraph(self):
        print("Sorry, this feature has not been implemented yet.\n")

    def setRunningFalse(self):
        self.running = False

    def checkUserChoice(self):
        if self.choice == "1":
            self.addWeight()
        elif self.choice == "2":
            self.showData()
        elif self.choice == "3":
            self.showGraph()
        elif self.choice == "4":
            self.setRunningFalse()
        else:
            print("Invalid number choice, please choose a valid number choice")
