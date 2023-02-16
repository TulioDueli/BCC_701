import math
L = float(input('Forneça o cumprimento do fio: '))
P = float(input('Forneça a força peso: '))
m = float(input('Forneça a massa: '))
g = P / m
pi = 3.14
T = 2 * pi * math.sqrt(L / g)
print(f'A aceleração da gravidade é: {g:.3f}')
print(f'O período do pêndulo é: {T:.3f}')