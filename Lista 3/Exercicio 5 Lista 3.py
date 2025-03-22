A = int(input('Numero 1: '))
B = int(input('Numero 2: '))

if a == 0 or b == 0:
    print('Numero não pode ser igual a 0')
else:
    if b > a:
        a, b = b, a
    while b != 0:
        c = a
        a = b
        b = c
        b = c % b
    print(a,'É o MDC')
    
