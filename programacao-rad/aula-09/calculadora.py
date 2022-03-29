def entrada_dados():
    operador1 = float(input('Operando 1: '))
    operador2 = float(input('Operando 2: '))
    return operador1, operador2


def adicao(op1, op2):
    print('*** ADIÇÃO ***')
    resultado = op1 + op2
    return resultado


def subtracao(op1, op2):
    print('*** SUBTRAÇÃO ***')
    resultado = op1 - op2
    return resultado


def divisao(op1, op2):
    print('*** DIVISÃO ***')
    resultado = op1 / op2
    return resultado


def multiplicacao(op1, op2):
    print('*** MULTIPLICAÇÃO ***')
    resultado = op1 * op2
    return resultado


def cai_fora():
    print('\nTchau!\n')
    quit()


def menu():
    escolha = 0
    while escolha != 5:
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair')
        escolha = int(input('Faça sua escolha: '))

        if escolha == 1:
            (op1, op2) = entrada_dados()
            resultado = adicao(op1, op2)
        elif escolha == 2:
            (op1, op2) = entrada_dados()
            resultado = subtracao(op1, op2)
        elif escolha == 3:
            (op1, op2) = entrada_dados()
            resultado = multiplicacao(op1, op2)
        elif escolha == 4:
            (op1, op2) = entrada_dados()
            resultado = divisao(op1, op2)
        elif escolha == 5:
            cai_fora()

        print('O resultado é: ', resultado)


menu()
