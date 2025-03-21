anos = 0
A = 80000
B = 200000
while True:
    if A >= B:
        print(anos, ' anos')
        break
    else:
        A = A + A * 0.03
        B = B + A * 0.015
        anos = anos + 1
