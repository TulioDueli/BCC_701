x = float(input('Quantidade de Morangos (em kg): '))
y = float(input('Quantidade de Maçãs (em kg): '))
if x < 0 or y < 0:
    print('Entrada inválida')
else:
    if x <=5:
        z = (2.50 * x)
    else:
        z = (2.20 * x)
    if y <=5:
        z1 = (1.80 * y)
    else:
        z1 = (1.50 * y)
    w = z + z1
    print(f'O valor total da sua compra é R$ {w: .2f}')