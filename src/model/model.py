from .sector import Sector

class Model(object):
    def __init__(self, name) -> None:
        self.__root = Sector(name)
    
    def GetRoot(self):
        return self.__root

    def __str__(self):
        return "Model: " + str(self.__root)

    def GetAllLeaves(self):
        rst = []
        node = [self.__root]
        while node:
            cur = node.pop(0)
            sub_sectors = cur.getSubSectors()
            if not sub_sectors:
                rst.append(cur)
            else:
                node.extend(sub_sectors)
        return rst

