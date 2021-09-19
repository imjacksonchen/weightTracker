# User class to hold name and __data

class User:

    ### Instance Variables ###
    __userName = ""
    __validUser = None
    __data = None
    ##########################

    ### Getters ###
    def getUserName(self):
        return self.__userName

    def getData(self):
        return self.__data

    def getValidUser(self):
        return self.__validUser
    ################

    ### Setters ###
    def setUserName(self, name):
        self.__userName = name

    def setData(self, data):
        self.__data = data

    def setValidUser(self, valid):
        self.__validUser = valid
    ################
