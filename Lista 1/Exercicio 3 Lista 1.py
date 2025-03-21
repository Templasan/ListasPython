def contador():
    DIAS = int(input('Insira o número de dias:'))
    HORAS = int(input('Insira o número de horas:'))
    MINUTOS = int(input('Insira o número de minutos:'))
    SEGUNDOS = int(input('Insira o número de segundos:'))
    VSEG = DIAS*86400 + HORAS*3600 + MINUTOS*60 + SEGUNDOS
    print(VSEG)
while True:
    contador()
    
