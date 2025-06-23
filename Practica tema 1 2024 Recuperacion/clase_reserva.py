
class Reserva:
    __numero_reserva:int
    __nombre_persona:str
    __nro_cabania:int
    __fecha_reserva:str
    __huespedes:int
    __dias:int
    __senia:float

    def __init__(self,numero_reserva,nombre_persona,nro_cab,fecha_reserva,huespedes,dias,senia):
        self.__numero_reserva = numero_reserva
        self.__nombre_persona = nombre_persona
        self.__nro_cabania = nro_cab
        self.__fecha_reserva = fecha_reserva
        self.__huespedes = huespedes
        self.__dias = dias
        self.__senia = senia
    
    def get_nro_reserva(self):
        return self.__numero_reserva
    def get_nombre_persona(self):
        return self.__nombre_persona
    def get_nro_cabania(self):
        return self.__nro_cabania
    def get_fecha_reserva(self):
        return self.__fecha_reserva
    def get_huespedes(self):
        return self.__huespedes
    def get_dias(self):
        return self.__dias
    def get_senia(self):
        return self.__senia
    def __lt__(self,otro_huesped):
        return self.__huespedes < otro_huesped.get_huespedes()