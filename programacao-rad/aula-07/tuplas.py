minha_tupla = ('t', 'u', 'p', 'l', 'a')
print(minha_tupla, type(minha_tupla))
print('-=' * 15)

# slice
print(minha_tupla[1:3])
print(minha_tupla[2:])
print(minha_tupla[:3])
print(minha_tupla[:])
print('-=' * 15)

# verifica quantos elementos existem na tupla
print(len(minha_tupla))
print(len(('Olá', 'mundo', 'do', 'Python')))
print('-=' * 15)

# concatenar tuplas
parte1 = ('Ouviram', 'do', 'ipiranga')
parte2 = ('as', 'margens', 'plácidas')
verso1 = parte1 + parte2
print(verso1)
print('-=' * 15)

# repetir elementos
mi = ('mi',)
print(mi * 5)
print('-=' * 15)

# verificar se elemento pertence a tupla
print('u' in minha_tupla)
print('f' in minha_tupla)
print('-=' * 15)

# iterar nos elementos
for i in minha_tupla:
    print(i)
