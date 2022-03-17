class Contato:
    todos_contatos = []

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Contato.todos_contatos.append(self)


class Fornecedor(Contato):

    def pedido(self, pedido):
        return f'pedido {pedido} feito por {self.nome}'


class Amigo(Contato):

    def __init__(self, nome, email, telefone):
        super().__init__(nome, email)
        self.telefone = telefone


c = Contato('Pietro', 'pietro@teste.com')
f = Fornecedor('FornecedorX', 'fornecedorx@teste.com')

print(c.nome, c.email)
print(f.nome, f.email)

print(f.pedido('Ped0001'))
