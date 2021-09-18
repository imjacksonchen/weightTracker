# User class to hold name and data

class User:
    userName = ""
    validUser = False
    data = None

    def setUserName(self, name):
        self.userName = name

    def getUserName(self):
        return self.userName

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
