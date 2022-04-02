a = '10'
print(a * 2)
print('-=' * 10)


class FormaGeometrica:
    pass


class Quadrado(FormaGeometrica):
    pass


def fatorial(valor):
    if valor == 0:
        return 1
    else:
        return valor * fatorial(valor - 1)


print(fatorial(5))
print('-=' * 10)


class Vendas:
    def __init__(self, id1):
        self.id1 = id1
        id1 = 100


val = Vendas(123)
print(val.id1)
