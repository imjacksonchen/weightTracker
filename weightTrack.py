# Weight Tracker app

""" 
To Do:
1. Be able to log time, weight, and note of a weighing
2. Use the weights to create a graph and show changes in weight over time

Notes:
- Using text files for storage/databse for weight information
  possibly move to a more reliable database method such as pickle/sqlite
- Add a user interface to navigate if they want to add a new entry, look at old
  entries, or view graphs
- Making validUser a "state" in User class? more object oriented
- Main is basically to just start application and connect classes together.


Questions:
1. Should user be able to change their note? Therefore setting a new time
    Argument for no: I wouldn't be able to remember an old weight or what i
    did after a day. Therefore allow for up to 30 min of change time else,

"""

from WeightNote import WeightNote
from File import File
from User import User
import matplotlib as plt

FILE_NAME = "weights.txt"

# Change function to be more independent by accepting a file name


# Main
if __name__ == '__main__':
    print("---------------------")

    # Load database if possible
    user = User()
    f = File(FILE_NAME)

    f.loadFile()
    user.setUserName(f.extractUserName())
    user.setData(f.loadUserData())

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
            note = input("Any Note? ")
            print("Adding entry...")
            curWeight = WeightNote(weight, note)

            # confirmation
            print("You just recorded {} pounds and your note is: '{}' on {} at {}".format(
                curWeight.getWeight(), curWeight.getNote(), curWeight.getTime().strftime("%m/%d/%Y"), curWeight.getTime().strftime("%H:%M")))

            # Saving it to a textfile
            with open("weights.txt", "a") as f:  # in append mode
                f.write("{}\n".format(curWeight))
            data.append(curWeight)  # need to be changed
            print("Entry saved")
        elif choice == "2":  # look at all entry
            # To do: make this into a function part of the class
            count = 1
            for entry in user.getData():
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
    # note = input("Any Note? ")
    # curWeight = WeightNote(weight, note)

    # # confirmation
    # print("You just recorded {} pounds and your note is: '{}' on {} at {}".format(curWeight.weight, curWeight.note, curWeight.time.strftime("%m/%d/%Y"), curWeight.time.strftime("%H:%M")))

    # # Saving it to a textfile
    # with open("weights.txt", "a") as f: # in append mode
    #     f.write("{}\n".format(curWeight))
    #     print("Entry saved")
