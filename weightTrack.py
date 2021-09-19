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

from Interface import Interface

FILE_NAME = "weights.txt"

# Main
if __name__ == '__main__':

    interface = Interface()
    interface.loadInformation(FILE_NAME)

    interface.startInterface()

    while (interface.running):
        interface.userChoices()
        interface.askForUserChoice()
        interface.checkUserChoice()
