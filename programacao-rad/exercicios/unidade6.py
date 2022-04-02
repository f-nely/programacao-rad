lista = [4, 2, 1, 5, 0]
lista.sort()
print(lista)
print('-=' * 10)

pilha = []
pilha.insert(0, 10)
pilha.insert(0, 5)
pilha.insert(0, 3)
pilha.insert(0, 40)
pilha.pop(0)
pilha.insert(0, 11)
pilha.insert(0, 4)
pilha.insert(0, 7)
pilha.pop(0)
pilha.pop(0)
print('Piha:', pilha)
print('-=' * 10)

fila = list()
fila.append(10)
fila.append(3)
fila.append(5)
fila.append(8)
fila.pop(0)
fila.pop(0)
fila.append(20)
print('Fila:', fila)
print('-=' * 10)

stack = []
stack.insert(0, 10)
stack.insert(0, 50)
stack.insert(0, 40)
stack.insert(0, 120)
stack.pop(0)
stack.insert(0, 15)
stack.pop(0)
stack.pop(0)
print('Pilha:', stack)
print('-=' * 10)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista1 + lista2)
