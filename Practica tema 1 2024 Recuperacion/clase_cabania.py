
class Cabania:
    __numero:int
    __cant_hab:int
    __cant_camas_grandes:int
    __cant_camas_chicas:int
    __importe_dia:float


    def __init__(self,numero,cant_hab,cant_camas_grand,cant_camas_chicas,importe_dia):
        self.__numero = numero
        self.__cant_hab = cant_hab
        self.__cant_camas_grandes = cant_camas_grand
        self.__cant_camas_chicas = cant_camas_chicas
        self.__importe_dia = importe_dia
    
    def get_numero(self):
        return self.__numero
    
    def getCanthabitacion(self):
        return self.__cant_hab
    
    def get_CantCamasGrandes(self):
        return self.__cant_camas_grandes
    
    def get_CantCamasChicas(self):
        return self.__cant_camas_chicas
    
    def get_importe_dia(self):
        return self.__importe_dia
    
    def __ge__(self):
        capacidad_cabania = self.get_CantCamasGrandes() * 2 + self.get_CantCamasChicas()
        return capacidad_cabania >= capacidad_cabania
    
    def __lt__(self,otro_numero):
        return self.__numero < otro_numero.get_numero()