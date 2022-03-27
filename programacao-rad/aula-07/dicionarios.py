# criando dicionários
contatos = {}
print(contatos)
print('-=' * 15)

# inserir dados no dicionário
contatos['Felix'] = ['1111-2222']
tel_brito = ['2221-3321', '3322-3333']
contatos['Brito'] = tel_brito
contatos['Piazza'] = ['4444-4441']
contatos['Carlos Alberto'] = ['4444-5541', '7777-4545']
tel_clodoaldo = ['3333-9999', '8888-3333', '8888-3434']
contatos['Clodoaldo'] = tel_clodoaldo
print(contatos)
print('-=' * 15)

# acessar dados no dicionário
print(contatos['Felix'])
tel_capitao = contatos['Carlos Alberto']
print(tel_capitao)
print('-=' * 15)

# alterar o conteúdo de alguma chave no dicionário
contatos['Felix'] = ['9999-1010']
print(contatos['Felix'])
print('-=' * 15)

# métodos para dicionário
print(contatos.keys())
print(contatos.values())
print(contatos.get('Brito'))
print(contatos.get('Rivelino'))
print(contatos.get('Piazza'))
print('Piazza' in contatos)
print('Guanabara' in contatos)
print(contatos.items())
jogadores = contatos.copy()
print(jogadores)
jogadores.clear()
print(jogadores)
print('-=' * 15)

# outras formas de cria dicionários
camisas = dict([(7, 'Jairzinho'), (9, 'Tostão'), (10, 'Lucas Paquetá'), (11, 'Rivelino')])
print(camisas)
print(camisas[7])
print(camisas[10])
print({}.fromkeys([16, 4, 2, 3]))
print({}.fromkeys([16, 4, 2, 3], 'defesa'))
