def calculadora():
    n = int(input('Insira a quantidade de cigarros por dia:'))
    t = float(input('Insira a quantos anos fuma:'))
    if n < 0:
        print('Quantidade de cigarros abaixo de zero')
        if t < 0:
            print('Tempo de fumo abaixo de zero')
    else:        
        tp = n*10/1440*t*365
        print(f'Dias perdidos:{tp}')
while True:
    calculadora()
    

