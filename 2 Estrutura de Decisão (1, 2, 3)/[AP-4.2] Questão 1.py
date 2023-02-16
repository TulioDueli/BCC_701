C = float(input('Capital emprestado: '))
m = int(input('Quantidade de meses para quitação: '))
if C <= 10000:
    t = 0.1
else:
    t = 0.07
J = C * t * m
total = J + C
print(f'Taxa de juros aplicada: {t * 100: .0f}%')
print(f'Juros devido: {J: .2f}')
print(f'Valor total: {total: .2f}')