"""
Criando e abrindo arquivos
'r' - leitura
'w' - escrita. substitui o conteúdo do arquivo existente
'x' - escrita. retorna um erro caso o arquivo já exista
'a' - escrita. insere os novos dados no final do arquivo
'b' - modo binário
't' - modo de texto (padrão)
'+' - atualizar. tanto leitura quanto escrita
"""
a = open('ajax_info.html', 'r')
print(a)

# iterar em um arquivo
# for linha in a:
#     print(linha)

# ler todas as linhas de um arquivo
# conteudo = a.read()
# print(conteudo)

# ler todas as linhas em uma lista
# a = open('ajax_info.html')
# lista = a.readlines()
# print(lista)

# ler o arquivo linha por linha
# a = open('ajax_info.html')
# lin1 = a.readline()
# print(lin1)
# lin2 = a.readline()
# print(lin2)
# lin3 = a.readline()
# print(lin3)
# lin4 = a.readline()
# print(lin4)

# criar um arquivo vazio
# b = open('new_file.txt', 'w')

# apagar o conteúdo de um arquivo
# escrever em um arquivo texto
# b = open('new_file.txt', 'w')
# b = open('new_file.txt')
# b.write('Ouviram do Ipiranga as margens plácidas')
# print(b.readline())

a.close()
