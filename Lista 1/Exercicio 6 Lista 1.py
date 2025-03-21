def calculadora():
    d = float(input('Insira a distância em kms:'))
    if d < 0:
        print('Valor da distãncia abaixo de zero')
    else:        
        vm = float(input('Insira a velocidade média:'))
        if vm < 0:
            print('Velocidade média abaixo de zero')
        else:
            t = d/vm 
            print(f'Tempo de viajem:{t}'' Horas')
while True:
    calculadora()
    
