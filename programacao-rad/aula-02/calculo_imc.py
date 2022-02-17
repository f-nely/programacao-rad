altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif imc >= 18.5 and imc <= 24.9:
    print('Parabẽns - você está em seu peso normal!')
elif imc >= 25.0 and imc <= 29.9:
    print('Você está acima de seu peso (sobrepeso)')
elif imc >= 30.0 and imc <= 34.9:
    print('Obesidade grau I')
elif imc >= 35.0 and imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')

print(f'Seu imc é {imc}')
