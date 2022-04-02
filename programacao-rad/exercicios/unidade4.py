def IMC(peso, altura):
    calculo = float(peso) / float(altura) * float(altura)
    return calculo


print(IMC(120, 1.98))
print('-=' * 10)


class Carro:
    def acelerar(self, vel):
        pass


class Funcionario:
    def __init__(self, matricula, nome, cargo):
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo


"""
Funções: 
    getattr - retorna o valor do atributo, 
    hasattr - testa se existe o atributo, 
    setattr - seta o valor do atributo, 
    delattr - remove o atributo, expattr - não existe.
"""
funcionario1 = Funcionario('3000241', 'Raphael', 'Gerente')
print(getattr(funcionario1, 'nome'))
