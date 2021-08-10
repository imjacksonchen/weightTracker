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
"""

import datetime
import matplotlib as plt

class WeightNote:
    def __init__(self, weight, notes):
        WeightNote.time = datetime.datetime.now() # use datetime to get current time 
        WeightNote.weight = weight
        WeightNote.notes = notes

    def __str__(self):
        return "{};{};{}".format(self.weight, self.notes, self.time)

# Main
if __name__ == '__main__':
    # Load database if possible
    newUser = False

    print("---------------------")

    try:
        f = open("weights.txt", "r")
    except IOError as error: # if file doesn't exist, create one
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
        data = line.split(";")
        parsedData = " | ".join(data)
        print("Entry {}: Weight: {}, Notes: {}, Date: {}".format(count, data[0], data[1], data[2]))
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
        if choice == "1": # add
            # To do: make this into a function part of the class
            weight = input("What was your recorded weight? ")
            notes = input("Any Notes? ")
            print("Adding entry...")
            curWeight = WeightNote(weight, notes)

            # confirmation
            print("You just recorded {} pounds and your note is: '{}' on {} at {}".format(curWeight.weight, curWeight.notes, curWeight.time.strftime("%m/%d/%Y"), curWeight.time.strftime("%H:%M")))

            # Saving it to a textfile
            with open("weights.txt", "a") as f: # in append mode
                f.write("{}\n".format(curWeight))
            history.append(curWeight)
            print("Entry saved")
        elif choice == "2": # look at all entry
            # To do: make this into a function part of the class
            count = 1
            for entry in history:
                print("{}: {}".format(count,entry))
                count += 1
        elif choice == "3": # make a graph using matplot
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

    