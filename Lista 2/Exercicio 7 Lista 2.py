m2 = int(input('Insira a area em m2 a ser pintada:'))
if m2 % 54 != 0:
    print(f'{m2 // 54 + 1} Lata Preço total {(m2 // 54 + 1)*80} Reais')
else:
    print(f'{m2 // 54} Lata Preço total {(m2 // 54)*80} Reais')
