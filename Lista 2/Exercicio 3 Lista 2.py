peixe = float(input('Insira o peso do peixe em quilos:'))
excesso = 'ZERO'
multa = 'ZERO'
if peixe > 50:
    excesso = peixe - 50
    multa = excesso * 4
    print(excesso,'quilos', multa,'reais' )
else:
    print(excesso, multa)
    
    
