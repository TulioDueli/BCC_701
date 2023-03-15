t= float(input('Defina o valor total da compra: R$ '))
if t <= 0:
    print('Erro: Valor total inválido.')
else:
    if t<=250:
        print('Desconto de 3%.')
        x=t-(0.03 * t)
    elif t>250 and t<=550:
        print('Desconto de 6%.')
        x=t-(0.06*t)
    elif t>550 and t<=750:
        print('Desconto de 8%.')
        x=t-(0.08*t)
    elif t>750:
        print('Desconto de 10%.')
        x=t-(0.1*t)
    print(f'Valor com desconto: R$ {x:.2f}')
    
