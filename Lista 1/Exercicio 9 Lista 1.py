def calculadora():
    d = float(input('Insira a distância em kms:'))
    t = int(input('Insira o número de dias alugados'))
    if d < 0:
        print('Valor da distãncia abaixo de zero')
        if t < 0:
            print('Número de dias abaixo de zero')
    else:        
        tp = t*60 + d*0.15
        print(f'Total a pagar:{tp}')
while True:
    calculadora()
    

