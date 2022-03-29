# def temp_f(temp_c):
#     valor = (temp_c*9/5) + 35
#     return valor


# temp = float(input('Digite a temperatura em graus Celsius: '))

# print('O valor da temperatura em graus Fahrenheit é:', temp_f(temp))

def temperatura(c):
    f = (c * 9 / 5) + 32
    k = c + 273
    return f, k


# (tempf, tempk) = temperatura(25)
# print('ºC = 25,ºF = ', tempf)
# print('ºC = 25, k = ', tempk)

def temp_f(temp_c=25):
    return (temp_c * 9 / 5) + 35


# print('Chamando a função com valor padrão. ºC = 25, ºF = ', temp_f())

# def funcao():
#     print(x)
#
#
# x = 'Teste'
# funcao()

# def funcao():
#     x = 'Olá mundo!'
#     print(x)
#
#
# x = 'Teste'
# funcao()
# print(x)

# def funcao():
#     print(x)
#     x = 'Olá mundo!'
#     print(x)
#
#
# x = 'Teste'
# funcao()
# print(x)

def funcao():
    global x
    print(x)
    x = 'Olá mundo!'
    print(x)


x = 'Teste'
funcao()
print(x)
