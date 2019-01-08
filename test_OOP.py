class Catalog():
    def __init__(self, id_name, id, name, ierarchy=False, parent=""):
        self.__id_name = id_name
        self.__id = id
        self.__name = name
        self.__ierarchy = ierarchy
        self.__parent = parent

    @property
    def id_name(self):
        return self.__id_name

    @id_name.setter
    def id_name(self, value):
        self.__id_name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def ierarchy(self):
        return self.__ierarchy

    @ierarchy.setter
    def id_name(self, value):
        self.__ierarchy = value

    @property
    def parent(self):
        return self.__ierarchy

    @parent.setter
    def parent(self, value):
        self.__parent = value

    def this_group(self):
        if self.__ierarchy and self.__parent != "":
            return True
        else:
            return False

    def put_in_base(self, id, name, parent):
        dict = {

        }

    def __repr__(self):
        return "CatalogManager: {0}".format(self.__id_name)


ctLog1 = Catalog("contragents", "", "", True)

print(ctLog1)



