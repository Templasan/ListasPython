a = float(input())
b = float(input())
c = float(input())
if a < b + c and b < a + c and c < a + b:
    print('É um triângulo')
    if a == b and b == c:
        print('É equilatero')
    elif a == b or a == c or b == c:
        print('É isóceles')
    else:
        print('Escaleno')
else:
    print('não é')
