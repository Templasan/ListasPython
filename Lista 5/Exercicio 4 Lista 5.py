def QuestãoD():
    lista = []
    for i in range(18644, 33088):
        i = str(i)
        if '2' in i and not '7' in i:
            lista.append('oi')
    print(len(lista))

QuestãoD()
