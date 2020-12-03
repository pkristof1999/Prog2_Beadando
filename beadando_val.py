#NOT FINISHED

class Values:
    def __init__(self, kliszt = "0", viz = "0", eleszto = "0",
                 so = "0", fliszt = "0", db = "0", ido = 0):
        self.__kliszt = str(kliszt)
        self.__viz = str(viz)
        self.__eleszto = str(eleszto)
        self.__so = str(so)
        self.__fliszt = str(fliszt)
        self.__db = str(db)
        self.__ido = str(ido)
    
    def getKliszt(self):
        return self.__kliszt
    
    def getViz(self):
        return self.__viz
    
    def getEleszto(self):
        return self.__eleszto
    
    def getSo(self):
        return self.__so
    
    def getFliszt(self):
        return self.__fliszt
    
    def getDb(self):
        return self.__db

    def getIdo(self):
        return self.__ido

    def setKliszt(self, kliszt):
        self.__kliszt = kliszt
    
    def setViz(self, viz):
        self.__viz = viz
    
    def setEleszto(self, eleszto):
        self.__eleszto = eleszto
    
    def setSo(self, so):
        self.__so = so
    
    def setFliszt(self, fliszt):
        self.__fliszt = fliszt
    
    def setDb(self, db):
        self.__db = db
    
    def setIdo(self, ido):
        self.__ido = ido