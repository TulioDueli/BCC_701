x = input('Entre com o nome: ')
y = float(input('Entre com a idade: '))
z = input('Entre com o sexo (m ou f): ')
if y >= 18 and z == 'm':
    print(f'{x} tem maioridade civil')
if z == 'm' and y < 18:
    y1 = 18 - y
    print(f'Faltam {y1: .1f} anos para {x} atingir a maioridade')
if y >= 21 and z == 'f':
    print(f'{x} tem maioridade civil')
if z == 'f' and y < 21:
    y2 = 21 - y
    print(f'Faltam {y2: .1f} anos para {x} atingir a maioridade')
    





