m14 = float(input('Média móvel dos últimos 14 dias: '))
a6 = int(input('Somatório dos casos dos últimos 6 dias: '))
h = int(input('Quantidade de casos de hoje: '))
m7 = (a6 + h) / 7
d = m7 - m14
x = (d / m14) * 100
if x < 0:
    x1 = x * (-1)
    print(f'Casos diminuindo em {-x: .2f}%')
else:
    if x <= 15:
        print(f'Casos estáveis em {x: .2f}%')
    else:
        print(f'Casos aumentando em {x: .2f}%')
