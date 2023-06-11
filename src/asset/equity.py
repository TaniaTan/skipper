from .security import Security
class Equity(Security):
    def __init__(self, name):
        super().__init__()
        self.__name = name
    def getName(self):
        return self.__name