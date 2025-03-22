import random

lista1 = random.sample(range(1, 101), 10)
lista2 = random.sample(range(1, 101), 10)
lista = []
x = 0
while x < 10:
    lista.append(lista1[x])
    lista.append(lista2[x])
    x = x + 1

print(lista)
print(len(lista))
