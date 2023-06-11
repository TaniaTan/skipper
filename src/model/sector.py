class Sector():
    def __init__(self, name):
        self.__name = name
        self.__security_children = []
        self.__sector_children = []
        self.__parent = None
    
    def getName(self):
        return self.__name

    def setParent(self, parent):
        self.__parent = parent

    def addSecurity(self, security):
        if self.__sector_children:
            raise Exception("can not add security to a non-leaf sector")
        self.__security_children.append(security)

    def addSector(self, sector):
        if self.__security_children:
            raise Exception("can not add sector to leaf sector")
        self.__sector_children.append(sector)
        sector.setParent(self)

    def getSecurities(self):
        if self.__security_children:
            return self.__security_children
        else:
            rst = []
            for sub_sector in self.__sector_children:
                rst.extend(sub_sector.getSecurities())
            return rst
        
    def getSubSectors(self):
        if self.__sector_children:
            return self.__sector_children
        else:
            return None
    def __str__(self):
        return self.__name
    
    def __le__(self, rhs):
        return self.__name < rhs.__name

    def getPath(self):
        rst = [str(self)]
        cur = self
        while cur.__parent:
            rst.append(str(cur.__parent))
            cur = cur.__parent
        return "/".join(rst[::-1])
    