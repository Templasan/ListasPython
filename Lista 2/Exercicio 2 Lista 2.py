def bissextos():
    ano = int(input("Insira o ano:"))
    if ano % 4 == 0 or ano % 100 != 0 and ano % 400 == 0:
              print("Ele é bissexto")
    else:
        print("Ele não é bissexto")
        
    
while True:
    bissextos()
