m = float(input('Média no semestre: '))
f = int(input('Frequência no semestre: '))
if m >= 6 and f >= 75:
    print('Conceito: aprovado')
else:
    if m < 6 and f > 75:
        x = 6 - m
        print(f'Conceito: exame especial\nJustificativa: média {x: .2f} abaixo da mínima')
    else:
        y = 75 - f
        print(f'Conceito: reprovado por faltas\nJustificativa: frequência {y}% abaixo da mínima')
        