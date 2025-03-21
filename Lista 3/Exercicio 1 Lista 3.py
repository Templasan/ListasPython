while True:
    nota = int(input('insira sua nota: '))
    if nota >= 0 and nota <= 10:
        print('Nota Valida')
        break
    else:
        print('nota invalida')
    
