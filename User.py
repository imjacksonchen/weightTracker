# User class to hold name and __data

class User:

    ### Instance Variables ###
    __userName = ""
    __validUser = None
    __data = []

    __weights = []
    __notes = []
    __dates = []

    __avgWeight = 0
    ##########################

    ### Getters ###
    def getUserName(self):
        return self.__userName

    def getData(self):
        return self.__data

    def getValidUser(self):
        return self.__validUser

    def getWeights(self):
        return self.__weights

    def getNotes(self):
        return self.__notes

    def getDates(self):
        return self.__dates

    def getAvgWeight(self):
        return str(self.__avgWeight)
    ################

    ### Setters ###
    def setUserName(self, name):
        self.__userName = name

    def setData(self, data):
        self.__data = data

    def setValidUser(self, valid):
        self.__validUser = valid

    def setWeights(self, weights):
        self.__weights = weights

    def setNotes(self, notes):
        self.__notes = notes

    def setDates(self, dates):
        self.__dates = dates
    ################

    def addData(self, data):
        self.__data.append(data)

    def addWeight(self, weight):
        self.__weights.append(weight)

    def addNote(self, note):
        self.__notes.append(note)

    def addDate(self, date):
        self.__dates.append(date)

    def calcAvg(self):
        weightData = self.getWeights()
        self.__avgWeight = int(self.sumOfWeights(weightData)/len(weightData))

    def sumOfWeights(self, weightData):
        weightSum = 0
        for weight in weightData:
            weightSum += int(weight)
        return weightSum
