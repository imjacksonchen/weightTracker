import datetime


class Weight:

    ### Instance Variables ###
    __time = None
    __weight = None
    __note = None
    ##########################

    ### Constructor ###
    def __init__(self, weight, note):
        self.__time = datetime.datetime.now()  # use datetime to get current time
        self.__weight = weight
        self.__note = note
    ###################

    ### Getter methods ###
    def getTime(self):
        return self.__time

    def getWeight(self):
        return self.__weight

    def getNote(self):
        return self.__note
    ######################

    ### Setter methods ###
    def setTime(self):
        pass

    def setWeight(self, weight):
        self.__weight = weight

    def setNote(self, note):
        self.__note = note

    def __str__(self):
        return "{};{};{}".format(self.__weight, self.__note, self.__time)
    ######################
