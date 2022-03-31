from math import pi


def area_circulo(raio):
    area = pi * pow(raio, 2)
    return round(area, 1)


r = int(input('Digite o raio do círculo: '))
print(f'A área do círculo de raio {str(r)} é {area_circulo(r)} m²')
