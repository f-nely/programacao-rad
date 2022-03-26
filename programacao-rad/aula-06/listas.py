from random import shuffle

lista = []
print(lista)
print('-=' * 15)

lista2 = ['Olá', 'mundo', 123]
print(lista2)
print(lista2[2])
print(lista2[0])
print('mundo' in lista)
print('mundo' in lista2)
print('-=' * 15)

lista_num = [10, 50, 40, 30, 50, 90, 70]
print(lista_num)
print(min(lista_num))
print(max(lista_num))
print(sum(lista_num))
print('-=' * 15)

# inserção de elementos
estados = ['SP', 'RJ', 'ES']
print(estados)
estados.append('MG')
print(estados)
print('-=' * 15)

# remoção de elementos
estados.pop(0)
print(estados)
estados.pop()
print(estados)
# Quando não conhecemos a posição do elemento que
# queremos eliminar usamos o método remove()
estados.remove('ES')
print(estados)
print('-=' * 15)

# inserção de elementos em posição específica
estados.insert(1, 'ES')
print(estados)
estados.insert(1, 'SP')
print(estados)
estados.insert(1, 'MG')
print('-=' * 15)

# ordenação dos elementos
estados.sort()
print(estados)
shuffle(estados)
print(estados)
estados.reverse()
print(estados)
print('-=' * 15)

# contagem de ocorrências de um elemento
print(estados)
estados.append('MG')
estados.append('MG')
print(estados)
print(estados.count('MG'))
print(estados.count('RJ'))
print('-=' * 15)

# retorno do índice da primeira ocorrência do elemento
estados = ['RJ', 'MG', 'SP', 'ES', 'MG', 'MG']
print(estados)
print(estados.index('MG'))
print('-=' * 15)

# prolongação
sul = ['PR', 'SC', 'RS']
print(sul)
estados = ['ES', 'MG', 'RJ', 'SP']
print(estados)
estados.extend(sul)
print(estados)
