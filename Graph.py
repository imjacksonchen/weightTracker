import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime

# Graph class potentially use inheritence to create pound vs kilogram graph


class Graph:

    def simpleGraph(self, dates, weights):
        fig, ax = plt.subplots()  # Create a figure containing a single axes
        # Plot some data on the axes (x, y)

        print(self.formatDate(dates))

        ax.plot(self.formatDate(dates), weights)

        ax.set(xlabel='Time', ylabel='Weight (lbs)',
               title='Progress')

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

        # beautify the x-labels
        plt.gcf().autofmt_xdate()

        # ax.grid()
        plt.show()

    def formatDate(self, dates):
        return list(map(datetime.datetime.strptime, dates, len(dates) * ['%Y-%m-%d "%H:%M:%"']))
