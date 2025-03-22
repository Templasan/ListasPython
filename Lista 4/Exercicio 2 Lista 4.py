import random

lista = random.sample(range(1, 101), 20)
PAR = []
IMPAR = []

for x in lista:
    if x % 2 == 0:
        PAR.append(x)
    else:
        IMPAR.append(x)

PAR.sort()
IMPAR.sort()
print(PAR)
print(IMPAR)
