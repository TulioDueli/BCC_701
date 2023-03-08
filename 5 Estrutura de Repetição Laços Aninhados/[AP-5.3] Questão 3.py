print('Caixa aberto!')
c= 'não'
p1=0
x=0
while c=='não' or c=='n' or c=='Não' or c=='nao':
    p1+=1
    p= int(input('\nQuantidade de itens do pedido: '))
    pre=0
    for i in range(1, p+1):
        pre+= float(input(f'. Preço do item {i}: '))
    d= input('. Cobrar delivery? ')
    if d=='sim':
        pre+=15
    print(f'. Valor do pedido: R$ {pre:.2f}.')
    x+=pre
    c= input('Fechar o caixa? ')
print('\nCaixa fechado!')
print(f'Número de pedidos: {p1}.')
print(f'Valor total vendido: R$ {x:.2f}.')
