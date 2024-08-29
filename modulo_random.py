import random

print("Número aleatorio del 1 al 1000: ", random.randrange(1000))
print("Lista aleatoria de números enre el 1 y el 100: ", random.sample(range(1000),3))
print("Número aleatorio en coma flotante o decimal: ", random.random())
print("Elección aleatoria [Python, Java, C#, Ruby, GO]: ", random.choice(['Python', 'Java', 'C#', 'Ruby', 'GO']))

