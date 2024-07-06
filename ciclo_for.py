lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
for item in lista:
    print(item, end=' ')
print("\n")

# Anidando bucles
lista_iteraciones = [1,2,3,4,5]
for item in lista_iteraciones:
    print("Iteracion numero: " + str(item))
    for item in lista:
        print(item, end=' ')
    print("\n")

# Con diferentes tipos de datos
lista_mixta = [99,'Casa',['Hola', 'Adios'], "Perro", 'Gato', 34]
for item in lista_mixta:
    print(item)

for item in range(5):
    for item2 in range(3):
        print("Iteracion " + str(item) + "," + str(item2))
