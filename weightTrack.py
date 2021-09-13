# Weight Tracker app

""" 
To Do:
1. Be able to log time, weight, and notes of a weighing
2. Use the weights to create a graph and show changes in weight over time

Notes:
- Using text files for storage/databse for weight information
  possibly move to a more reliable database method such as pickle/sqlite
- Add a user interface to navigate if they want to add a new entry, look at old
  entries, or view graphs


Questions:
1. Should user be able to change their notes? Therefore setting a new time
    Argument for no: I wouldn't be able to remember an old weight or what i
    did after a day. Therefore allow for up to 30 min of change time else,

"""

import datetime
import matplotlib as plt


class WeightNote:
    __time = None
    __weight = None
    __note = None

    def __init__(self, weight, note):
        self.__time = datetime.datetime.now()  # use datetime to get current time
        self.__weight = weight
        self.__note = note

    # Getter methods

    def getTime(self):
        return self.__time

    def getWeight(self):
        return self.__weight

    def getNote(self):
        return self.__note

    # Setter methods

    def setTime(self):
        pass

    def setWeight(self, weight):
        self.__weight = weight

    def setNote(self, note):
        self.__note = note

    def __str__(self):
        return "{};{};{}".format(self.weight, self.notes, self.time)


def loadUser():
    pass


# Main
if __name__ == '__main__':
    # Load database if possible
    newUser = False

    print("---------------------")

    try:
        f = open("weights.txt", "r")
    except IOError as error:  # if file doesn't exist, create one
        f = open("weights.txt", 'w')
        newUser = True

    # Load name
    if newUser == True:
        print("Hi! It seems that you're a new user. Welcome!")
        name = input("What is your name? ")
        f.write("{}\n".format(name))
    else:
        name = f.readline().strip()
        print("Hi {}! Welcome back!".format(name))

    # Load data if any
    # data order: 0: weight, 1: notes, 2: date and time
    lines = f.readlines()
    count = 1
    history = []

    for line in lines:
        # Change delimter because this can easily be broken
        data = line.split(";")
        parsedData = " | ".join(data)
        print("Entry {}: Weight: {}, Notes: {}, Date: {}".format(
            count, data[0], data[1], data[2]))
        history.append(parsedData)
        count += 1

    # Start user interface
    while True:
        print("1. Add entry")
        print("2. Look at all entry")
        print("3. Check out graph")
        print("4. Quit")
        choice = input("What would you like to do? (number input) ")

        # Switch/case but using if/elif since im running python 3.9
        if choice == "1":  # add
            # To do: make this into a function part of the class
            weight = input("What was your recorded weight? ")
            notes = input("Any Notes? ")
            print("Adding entry...")
            curWeight = WeightNote(weight, notes)

            # confirmation
            print("You just recorded {} pounds and your note is: '{}' on {} at {}".format(
                curWeight.weight, curWeight.notes, curWeight.time.strftime("%m/%d/%Y"), curWeight.time.strftime("%H:%M")))

            # Saving it to a textfile
            with open("weights.txt", "a") as f:  # in append mode
                f.write("{}\n".format(curWeight))
            history.append(curWeight)
            print("Entry saved")
        elif choice == "2":  # look at all entry
            # To do: make this into a function part of the class
            count = 1
            for entry in history:
                print("{}: {}".format(count, entry))
                count += 1
        elif choice == "3":  # make a graph using matplot
            # To do: make this into a function part of the class
            print("Sorry, feature has not been implemented.\n")
        elif choice == "4":
            # To do: make this into a function part of the class
            break
        else:
            print("Invalid number choice, please choose a valid number choice")

    print("---------------------")

    # weight = input("What was your recorded weight? ")
    # notes = input("Any Notes? ")
    # curWeight = WeightNote(weight, notes)

    # # confirmation
    # print("You just recorded {} pounds and your note is: '{}' on {} at {}".format(curWeight.weight, curWeight.notes, curWeight.time.strftime("%m/%d/%Y"), curWeight.time.strftime("%H:%M")))

    # # Saving it to a textfile
    # with open("weights.txt", "a") as f: # in append mode
    #     f.write("{}\n".format(curWeight))
    #     print("Entry saved")
