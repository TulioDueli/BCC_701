import math
q = int(input('Digite a quantidade de lados: '))
if q < 3:
    print('Não é um polígono')
if q == 3:
    L = float(input('Digite a medida do lado: '))
    A3 = (L**2 * (math.sqrt(3))) / 4
    print(f'O polígono é um triângulo com área: {A3: .2f}')
if q == 4:
    L = float(input('Digite a medida do lado: '))
    A4 = L**2 
    print(f'O polígono é um quadrado com área: {A4: .2f}')
if q == 5:
    L = float(input('Digite a medida do lado: '))
    A5 = (5 * (L**2)) / (4 * (math.tan(0.6283)))
    print(f'O polígono é um pentágono com área: {A5: .2f}')
if q == 6:
    L = float(input('Digite a medida do lado: '))
    A6 = (3 * L**2 * math.sqrt(3)) / 2
    print(f'O polígono é um hexágono com área: {A6: .2f}')
if q > 6:
    print('Polígono não identificado')