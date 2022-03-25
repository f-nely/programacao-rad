class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_idade(self):
        return self.idade


class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.cpf = cpf


class PessoaJuridica(Pessoa):
    def __init__(self, nome, idade, cnpj):
        super().__init__(nome, idade)
        self.cnpj = cnpj


p1 = Pessoa('Diana', 12)
print(id(p1))
print(p1.get_idade())

pf = PessoaFisica('Zé', 41, '123.456.789-00')