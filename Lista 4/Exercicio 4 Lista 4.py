texto = '''The Python Software Foundation and the global Pythoncommunity welcome and encourage participation by everyone.
Our community is based onmutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, andwhatever your background, we welcome you.'''
limpeza = ',.:'
for p in limpeza:
    texto = texto.replace(p, "")
texto = texto.lower()
    
lista = []
lista = texto.split(" ")
listapython = []
piton = 'python'
lpython = [s for s in lista if s[0] in piton or s[-1] in piton]
    
print(lista)
print(lpython)
