# Funciones y manejo de listas
lista = [45,32,3,78]
print("Lista original: ", lista)
lista.append(995)
lista.append(7)
print("Lista despues de usar append: ", lista)
lista.sort()
print("Lista ordenada: ", lista)
lista.reverse()
print("Lista al revés: ", lista)
lista_extend = [1,5,87,45]
lista.extend(lista_extend)
print("Lista despues de extend: ", lista)
lista.sort(reverse=True)
print("Lista ordenada al revés", lista)
print("Numero de veces encontrado el 45", lista.count(45))
lista.insert(4,111)
print("Lista despues de insert: ", lista)
lista.remove(45)
print("Lista despues de remove: ", lista)
print("Posicion del elemento 111", lista.index(111))
lista.pop()
print("Lista despues de pop: ", lista)
lista.clear()
print("Lista despues de clear: ", lista)


