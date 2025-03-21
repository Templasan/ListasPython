N = int(input('Insira o numero: '))
contador = 0
f1 = 1
f2 = 0
while contador != N:
    if contador % 2 == 0 and contador != 0:
        print(f2)
        f1 = f1 + f2
    else:
        print(f1)
        f2 = f2 + f1
    contador = contador + 1
