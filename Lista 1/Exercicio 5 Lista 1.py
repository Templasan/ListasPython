def calculadora():
    Preço = float(input('Insira o valor do produto:'))
    if Preço < 0:
        print('Valor do produto abaixo de zero')
    else:        
        Desconto = float(input('Insira o valor do desconto:'))
        if Desconto < 0:
            print('Valor de percentual abaixo de zero')
        else:
            Preçof = Preço - (Preço/100)*Desconto
            Descontof = Preço - Preçof
            print(f'Valor do produto com o desconto:{Preçof}')
            print(f'Valor do desconto:{Descontof}')
while True:
    calculadora()
    
