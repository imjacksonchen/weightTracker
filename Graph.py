import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime

# Graph class potentially use inheritence to create pound vs kilogram graph


class Graph:

    def simpleGraph(self, dates, weights):
        print(dates)
        print(weights)
        fig, ax = plt.subplots()  # Create a figure containing a single axes
        # Plot some data on the axes (x, y)

        ax.plot(self.formatDate(dates), self.formatWeights(weights))

        ax.set(xlabel='Time', ylabel='Weight (lbs)',
               title='Progress')

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))

        # beautify the x-labels
        plt.gcf().autofmt_xdate()

        # ax.grid()
        plt.show()

    def formatDate(self, dates):
        return mdates.datestr2num(dates)

    def formatWeights(self, weights):
        return list(map(int, weights))
