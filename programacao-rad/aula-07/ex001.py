# seila = {}
seila = dict()
seila[1] = 1
seila['1'] = 2
seila[1] += 1
print(seila)

soma = 0
for k in seila:
    soma += seila[k]

print(soma)
