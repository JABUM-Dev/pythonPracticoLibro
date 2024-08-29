# Las colas son estructuras tipo FIFO (Fist In Fist Out)

class Cola:
    def __init__ (self):
        self.__items = []
    
    def esta_vacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    
    def encolar (self, item):
        self.__items.insert(0, item)
    
    def desencolar (self):
        return self.__items.pop()
    
    def leer_primer_elemento (self):
        return self.__items[len(self.__items)-1]
    
    def numero_elementos (self):
        return len(self.__items)
    
    def mostrar_cola (self):
        print("Cola: ", self.__items, "<-- Primer elemento")


def simulador_cola():
    fin = False
    cola = Cola()
    while not(fin):
        opc = input("Opción: ")
        if (opc == '1'):
            item = input("Introduzca el elemento a encolar: ")
            cola.encolar(item)
            print("Elemento encolado: ", item)
        elif (opc == '2'):
            if cola.esta_vacia():
                print("La cola esta vacia, no puede desencolarse ningun elemento")
            else:
                item = cola.leer_primer_elemento()
                cola.desencolar()
                print("Elemento desencolado: ", item)
        elif (opc == '3'):
            if cola.esta_vacia():
                print("La cola esta vacia, no puede leerse ningun elemento")
            else:
                print("El primer elemento es: ", cola.leer_primer_elemento())
        elif (opc == '4'):
            print(f"La cola tiene {cola.numero_elementos()}, elementos")
        elif (opc == '5'):
            if cola.esta_vacia():
                print("La cola esta vacia")
            else:
                print("La cola no esta vacia")
        elif (opc == '6'):
            cola.mostrar_cola()
        elif (opc == '7'):
            fin = True

print("""
********************
Simulador de cola
********************
1) Encolar
2) Desencolar
3) Leer primer elemento
4) Numero de elementos
5) ¿Esta vacia?
6) Mostar cola
7) Salir
""")
simulador_cola()

