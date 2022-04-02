preco = 200

if preco > 120:
    preco = preco * 0.85
    print(preco)
print('-=' * 10)

i = 1
soma = sal = 0
while i <= 45:
    # sal = float(input('Salário: '))
    soma = soma + sal
    i = i + 1

# print('Total da folha de pagamento R$ ', soma)

if preco <= 10.00:
    print('Promo 10')
elif preco < 50.00:
    print('Promo 20')
else:
    print('Promo 30')
print('-=' * 10)

x = 10
soma = 0

while x > 0:
    x = x - 2
    print(x)
    soma = soma + x
print(soma)

valor = 7
print('-=' * 10)

while valor > 3:
    print(valor)
    valor -= 1

else:
    ultimo_valor = valor
    print(ultimo_valor)
