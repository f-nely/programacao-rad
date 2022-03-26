class Pilha:
    def __init__(self):
        self.dados = []

    def push(self, elemento):
        self.dados.insert(0, elemento)

    def pop(self):
        self.dados.pop(0)

    def show_elements(self):
        return self.dados


p1 = Pilha()
p1.push(1)
p1.push(2)
p1.push(3)
print(p1.show_elements())
p1.pop()
print(p1.show_elements())
