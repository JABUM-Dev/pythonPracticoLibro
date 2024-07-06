i = 0
while i < 10:
    print(i, end=' ')
    i = i + 1
print("\n")

pedir_numero = True
while pedir_numero:
    valor = int(input("Introduce un entero inferior a 10: "))
    if valor < 10:
        pedir_numero = False
print("FIN. ¡Ha intorducido un valor menor a 10!")
print("\n")

item1 = 0
while item1 < 5:
    item2 = 0
    while item2 < 3:
        print("Iteracion " + str(item1) + ',' + str(item2))
        item2 += 1
    item1 += 1

# Combinando ciclos
for item1 in range(5):
    item2 = 0
    while item2 < 3:
        print("Iteracion " + str(item1) + ',' + str(item2))
        item2 += 1

