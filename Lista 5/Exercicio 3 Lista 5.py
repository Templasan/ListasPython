def QuestãoC():
    lista = []
    for i in range(1067, 3628):
        if i % 2 == 0 and i % 7 == 0:
            lista.append('oi')
    print(len(lista))

QuestãoC()
