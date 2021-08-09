# Weight Tracker app
""" 
To Do:
1. Be able to log time, weight, and notes of a weighing
2. Use the weights to create a graph and show changes in weight over time


Notes:
- Using text files for storage/databse for weight information
"""
import datetime

class WeightNote:
    def __init__(self, weight, notes):
        WeightNote.time = datetime.datetime.now() # use datetime to get current time 
        WeightNote.weight = weight
        WeightNote.notes = notes

    def __str__(self):
        return "{} {} {}".format(self.weight, self.notes, self.time)

# Main
if __name__ == '__main__':
    weight = input("What was your recorded weight? ")
    notes = input("Any Notes? ")
    curWeight = WeightNote(weight, notes)

    # confirmation
    print("You just recorded {} pounds and your note is: '{}' on {} at {}".format(curWeight.weight, curWeight.notes, curWeight.time.strftime("%m/%d/%Y"), curWeight.time.strftime("%H:%M")))

    print(curWeight)

    with open("weights.txt", "w") as f: #i n write mode
        f.write("{}".format(curWeight))
        print("recording saved")