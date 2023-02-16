p= input('Informe o nome do Produto: ')
while p!='fim':
    v= float(input('Valor do pedido: R$ '))
    if p=='Pão de queijo':
        if v <= 50:
            d=0.1
        elif v>50 and v <= 100:
            d=0.12
        else:
            d=0.15
    else:
        if v <= 50:
            d=0.09
        elif v>50 and v <= 100:
            d=0.1
        else:
            d=0.11
    x= v-(d*v)
    print(f'percentual de desconto: {d * 100:.2f}%')
    print(f'Valor com desconto: R$ {x:.2f}')
    p= input('Informe o nome do Produto: ')
    