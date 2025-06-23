from clase_reserva import Reserva
import csv

class GestorReserva:
    __listado_reservas:list

    def __init__(self):
        self.__listado_reservas = []

    #cargar reservas

    def cargar_reservas(self,UnaReserva):
        if UnaReserva != None:
            self.__listado_reservas.append(UnaReserva)

    #Abrir archivo

    def abrir_archivo(self):
        bandera = False

        with open('reservas.csv') as archivo_reservas:
            bandera = False
            lector = csv.reader(archivo_reservas,delimiter=';')
            for fila in lector:
                if not bandera:
                    bandera = True
                else:
                    nuro_reserva = int(fila[0])
                    nombre = fila[1]
                    nuro_cabania = int(fila[2])
                    fecha = str(fila[3])
                    huespedes = int(fila[4])
                    dias = int(fila[5])
                    senia = float(fila[6])
                    UnaReserva = Reserva(nuro_reserva,nombre,nuro_cabania,fecha,huespedes,dias,senia)
                    self.cargar_reservas(UnaReserva)
    def ordenar(self):
        self.__listado_reservas.sort()

    #buscar cabanias libres

    def buscar_reserva(self,aux_huespedes):
        indice = 0
        encontrado = None
        bandera = False
        while not bandera and indice < len(self.__listado_reservas):
            if self.__listado_reservas[indice].get_huespedes() >= int(aux_huespedes):
                if self.__listado_reservas[indice].get_nro_reserva():
                    bandera = True
                    encontrado = self.__listado_reservas[indice]
                else:
                    indice += 1
            
        return encontrado

    #Tabla cabanias reservadas

    def tablas_reservas(self,fecha_aux,GC):
        importe_cobrar = 0.0
        encabezado = False
        existe_reserva = False
        for fila in self.__listado_reservas:
            if not encabezado:
                print(f"Reservas para la fecha{fecha_aux}")
                print("N° de cabaña     |   Importe diario      |   Cantidad de dias    |   Seña    |   Importe a cobrar\n")
                encabezado = True
            else:
                fecha_res = str(fila.get_fecha_reserva())
                if fecha_aux != fecha_res:
                    print(f"No se registro reservas para la fecha {fecha_aux}")
                else:
                    existe_reserva = True
                    nro_cabania = int(fila.get_nro_cabania())
                    importe_dia = float(GC.buscar_importe(nro_cabania))
                    importe_cobrar = fila.get_dias() * importe_dia - fila.get_senia()
                    print(f"{fila.get_nro_cabania():<15},{importe_dia:<15},{fila.get_dias():<15},{fila.get_senia():<15},{importe_cobrar:<15}",end='')
            
            