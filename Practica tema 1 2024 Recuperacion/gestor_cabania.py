from clase_cabania import Cabania
import csv
import numpy as np

class GestorCabanias:
    __cantidad:int
    __dimension:int
    __incremento = 10
    __listado_cabanias:np.ndarray

    def __init__(self,dimension):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__listado_cabanias = np.empty(self.__dimension,Cabania)
    
    #Cargar cabañas

    def cargarCabanias(self,Una_cabanias):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listado_cabanias.resize(self.__dimension)
        self.__listado_cabanias[self.__cantidad] = Una_cabanias
        self.__cantidad += 1
    
    #Abrir archivo

    def abrirArchivo(self):
        bandera = False
        with open('cabañas.csv') as archivo_cabanias:
            lector = csv.reader(archivo_cabanias,delimiter=';')
            for fila in lector:
                if not bandera:
                    bandera = True
                else:
                    numero = int(fila[0])
                    cant_h = int(fila[1])
                    camasGrandes = int(fila[2])
                    camasChicas = int(fila[3])
                    importe = float(fila[4])
                    unaCabania = Cabania(numero,cant_h,camasGrandes,camasChicas,importe)
                    self.cargarCabanias(unaCabania)            
    #inciso (a)
    def cabanias_sin_reserva(self,huespedes,GR):
        reserva_aux = GR.buscar_reserva(huespedes)
        for fila in self.__listado_cabanias:
            if reserva_aux is None and reserva_aux != fila.get_numero():
                print(f"No hay cabanias disponible la capacidad {huespedes}")
            else:
                
                print(f"Numeros de cabanias disponibles con capacidad mayor o igual a la ingresada->{fila.get_numero()}")
    
    #inciso (b)
    def buscar_importe(self,aux_cabania):
        indice = 0
        bandera = False
        encontrado = None
        while not bandera and indice < len(self.__listado_cabanias):
            if aux_cabania == self.__listado_cabanias[indice].get_numero():
                bandera = True
                encontrado = float(self.__listado_cabanias[indice].get_importe_dia())
            else:
                indice += 1
        return encontrado