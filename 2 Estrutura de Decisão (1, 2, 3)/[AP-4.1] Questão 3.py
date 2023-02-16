import math
tipo = (input('Tipo de ladrilho (1 ou 2): '))
area = float(input('Área da sala: '))

if tipo == '1':
    x = area / 80
    x1 = math.ceil(x)
    print(f'Quantidade de ladrilhos: {x1: .0f}')
else:
    y = area / 60
    y1 = math.ceil(y)
    print(f'Quantidade de ladrilhos: {y1: .0f}')