H = float(input('Digite a altura:'))
g = (input('Qual é o sexo (m ou f):'))

if g == 'm':
    c = (72.7 * H) - 58
else:
    c = (62.1 * H) - 44.7
print(f'O peso ideal é {c: .2f}')
    