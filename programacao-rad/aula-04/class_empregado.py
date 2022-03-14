class Empregado:
    contator = 0

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        Empregado.contator += 1

    def mostra_contador(self):
        return f'Número de empregados: {Empregado.contator}'

    def mostra_empregado(self):
        return f'Nome: {self.nome}, Salário {self.salario}'


emp1 = Empregado('Fabiano', 1000)
emp2 = Empregado('Pietro', 1400)

print(emp1.mostra_empregado())
print(emp2.mostra_empregado())

emp1.idade = 44
print(f'Nome: {emp1.nome} - Salário: {emp1.salario} - Idade: {emp1.idade}')

emp2.idade = 31
print(f'Nome: {emp2.nome} - Salário: {emp2.salario} - Idade: {emp2.idade}')

del emp1.idade

print(getattr(emp1, 'nome'))
print(hasattr(emp1, 'e-mail'))

