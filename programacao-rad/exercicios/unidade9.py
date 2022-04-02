def maior(a, b):
    if a > b:
        print(a, 'é o maior')
    elif a == b:
        print(a, 'é igual a', b)
    else:
        print(b, 'é o maior')


maior(4, 1)


def sp(x, y):
    return (x + y), (x * y)


print(sp(2, 3))
