

class Classifier(object):
    def __init__(self, column, model) -> None:
        self.__column = column 
        self.__model = model
        self.__lookup = {i.getName(): i for i in self.__model.GetAllLeaves()}


    def classification(self,securities):
        result = dict()
        for security in securities:
            security_sector_name = security.getColumnValue(self.__column)
            if security_sector_name in self.__lookup.keys():
                result[security.getName()] = self.__lookup[security_sector_name]
        return result