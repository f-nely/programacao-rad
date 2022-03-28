str1 = 'nabucodonosor'
print(str1)
p = str1[0].upper()
print(str1[0])
print(p)
# str1[0] = 'f'

# iterar em strings
for i in str1:
    print(i)
# slice
print(str1[:])
print(str1[0:5])
print(str1[:5])
print(str1[5:])
print(str1[-1])

# verifica se um caractere está na string
print('f' in str1)
print('n' in str1)

# tamanho da string
print(len(str1))

# converter a string para maiúsculas ou minúsculas
print(str1.upper())
print(str1.lower())

# verificar se a string contém caracteres alfabéticos
print(str1.isalpha())
str2 = 'nabucodonosor30'
print(str2.isalpha())

# retirar espaços em brando no início e no fim da string
str3 = '  nabucodonosor  '
print(str3)
print(str3.strip())

# juntar casa item da string por meio de um delimitador específico
a = '-'.join(str1)
print(a)
