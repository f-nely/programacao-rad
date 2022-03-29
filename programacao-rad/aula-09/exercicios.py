# x = 1
#
#
# def funcao():
#     global x
#     print('x = ', x)
#     x = 2
#     print('x  global =', x)
#
#
# funcao()
# print('Valor de x =', x)

# i = 1
#
#
# def funcao():
#     global i
#     for j in (1, 2, 3):
#         i += 1
#
#
# funcao()
# print(i)

# def maior(a, b):
#     if a > b:
#         print(a, 'é o maior')
#     elif a == b:
#         print(a, 'é igual a', b)
#     else:
#         print(b, 'é o maior')
#
#
# maior(3, 4)

def foo(x):
    if x == 1:
        return 1
    else:
        return x + foo(x - 1)


print(foo(4))
