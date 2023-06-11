from .security import Security
class Bond(Security):
    def __init__(self, name, date):
        super().__init__()
        self.__name = name
        self.__date = date
    def getName(self):
        return self.__name + " " + str(self.__date)
