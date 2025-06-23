from gestor_cabania import GestorCabanias
from gestor_reserva import GestorReserva
def test():
    print("1|Inicio     0|Terminar")
    inicio = input("Elija una opcion->")
    while inicio != '0':
        GC = GestorCabanias(10)
        GR = GestorReserva()
        GC.abrirArchivo()
        GR.abrir_archivo()
        GR.ordenar()
        print("a) Ver numeros de cabañas con capacidad mayor o igual a la cantidad de huespedes,\n"
        "b) Ver listado de reservas para una fecha")
        opcion = input("Elija una opcion->")

        if opcion == 'a':
            aux = int(input("Cantidad de huespedes->"))
            GC.cabanias_sin_reserva(aux,GR)
        elif opcion == 'b':
            aux = input("Ingrese fecha-->")
            GR.tablas_reservas(aux,GC)


        print("1|Inicio     0|Terminar")
        inicio = input("Elija una opcion->")



if __name__ == '__main__':
    test()