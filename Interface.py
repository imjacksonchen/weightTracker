from Weight import Weight
from User import User
from File import File


class Interface:
    running = None
    choice = ""

    def userChoices(self):
        print("1. Add entry")
        print("2. Look at all entry")
        print("3. Check out graph")
        print("4. Quit")

    def startInterface(self):
        self.running = True

    def askForUserChoice(self):
        self.choice = input("What would you like to do? (number input) ")

    def addWeight(self):
        # To do: make this into a function part of the class
        weight = input("What was your recorded weight? ")
        note = input("Any Note? ")
        print("Adding entry...")
        curWeight = Weight(weight, note)

        # confirmation
        print("You just recorded {} pounds and your note is: '{}' on {} at {}".format(
            curWeight.getWeight(), curWeight.getNote(), curWeight.getTime().strftime("%m/%d/%Y"), curWeight.getTime().strftime("%H:%M")))

        # Saving it to a textfile
        with open("weights.txt", "a") as f:  # in append mode
            f.write("{}\n".format(curWeight))
        data.append(curWeight)  # need to be changed
        print("Entry saved")

    def showData(self):
        count = 1
        for entry in user.getData():
            print("{}: {}".format(count, entry))
            count += 1

    def showGraph(self):
        print("Sorry, this feature has not been implemented yet.\n")

    def setRunningFalse(self):
        self.choice = False

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
