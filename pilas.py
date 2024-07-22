# Las PILAS son una estructura de dato con un modo de acceso LIFO 
# "Last In First Out" - "Ultimo en entrar primero en salir"

class Pila:
    def __init__(self):
        self.__items = []
    
    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    
    def Apilar(self, item):
        self.__items.append(item)
    
    def Retirar(self):
        self.__items.pop()
    
    def LeerCima(self):
        return self.__items[len(self.__items)-1]
    
    def NumeroElementos(self):
        return len(self.__items)
    
    def MostrarPila(self):
        print("Pila: ", self.__items, "<-- Cima")
    

def SimuladorPila():
    fin = False
    pila = Pila()
    while not(fin):
        opc = input("Opcion:")
        # Apilar
        if (opc == '1'):
            item = input("Introduzca elemento a apilar: ")
            pila.Apilar(item)
            print("Elemento apilado: ", item)
        # Retirar
        elif (opc == '2'):
            if pila.EstaVacia():
                print("La pila esta vacia, no puede retirarse ningun elemento")
            else:
                item = pila.LeerCima()
                pila.Retirar()
                print("Elemento retirado: ", item)
        # Leer Cima
        elif (opc == '3'):
            if pila.EstaVacia():
                print("La pila está vacia, no puede leerse la cima")
            else:
                print("La cima es: ", pila.LeerCima())
        # Numero de elementos
        elif (opc == '4'):
            print("La pila tienes ", pila.NumeroElementos(), " elementos")
        # ¿Esta vacia?
        elif opc == '5':
            if pila.EstaVacia():
                print("La pila está vacia")
            else:
                print("La pila NO está vacia")
        # Mostrar Pila
        elif opc == '6':
            pila.MostrarPila()
        # Salir
        elif opc == '7':
            fin = True


print("""**********************
Simulador PILA
**********************
Menú
1) Apilar
2) Retirar
3) Leer cima
4) Número de elementos
5) ¿Está vacía?
6) Mostrar PILA
7) Salir""")
SimuladorPila()

