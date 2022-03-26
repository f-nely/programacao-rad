class Fila:
    def __init__(self):
        self.dados = []

    def enqueue(self, elemento):
        self.dados.append(elemento)

    def dequeue(self):
        self.dados.pop(0)

    def show_elements(self):
        return self.dados


f1 = Fila()
f1.enqueue(3)
f1.enqueue(2)
f1.enqueue(1)
print(f1.show_elements())
f1.dequeue()
f1.dequeue()
f1.dequeue()
print(f1.show_elements())
