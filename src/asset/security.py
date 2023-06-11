class Security():
    """
    represents type of finacial value, unually in the form of equity, bond etc.
    """
    def __init__(self):
        self.__name = None
        self._columns = dict()
    def getName(self):
        return self.__name
    def getColumns(self):
        return self._columns
    
    def getColumnValue(self, column_name):
        if column_name not in self._columns.keys():
            raise Exception("key doesn't exist.")
        return self._columns[column_name]
    
    def setColumnValue(self, column_name, column_value):
        self._columns[column_name] = column_value

    def __str__(self) -> str:
        return self.getName()
    def __lt__(self, rhs):
        return self.getName() < rhs.getName()
    