line = 'teste, de, alguma, coisa'
print(line.split(','))
print('-=' * 20)

str1 = 'Phyton123'
print(str1, str1.isalpha())
print('-=' * 20)

s1 = 'ABCDEF'
s2 = 'GHIJKL'

print(s1[:2].join(s2[3:]))
print('-=' * 20)

disciplina = 'Programação |||'
print(disciplina.isalpha())

temas = open('palavras.txt', 'e')
"""
Para abrir um arquivo, o Python possui a função open().
Ela recebe dois parâmetros: o primeiro é o nome do arquivo a ser aberto, 
e o segundo parâmetro é o modo que queremos trabalhar com esse arquivo
'e' somente leitura, 'w' apenas escrita, 'a' inserção de dados escrito no final do arquivo, 
'r+' - leitura e escrita.
"""
