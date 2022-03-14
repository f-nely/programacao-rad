class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


p = Ponto(2, 3)
print(p.x)
print(p.y)

print('-' * 20)
q = Ponto(3, 2)
print(q.x)
print(q.y)

print('-' * 20)
print(p.getX())
print(p.getY())
