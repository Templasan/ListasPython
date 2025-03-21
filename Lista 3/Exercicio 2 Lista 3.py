while True:
    nome = input('Insira nome de usuario: ')
    senha = input('Insira senha: ')
    if nome != senha:
        break
    else:
        print('Nome não pode ser igual a senha')
