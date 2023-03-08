from biblioteca import*
import math
def calculaLucros(cox, qui, lc, lq):
    lucro = []
    for i in range(len(cox)):
        conta= cox[i]*lc+qui[i]*lq
        conta= round(conta, 2)
        lucro.append(conta)
    return lucro

cox= inputVetor('Vendas de coxinhas: ', int)
qui= inputVetor('Vendas de quibes: ', int)
if len(cox)!=len(qui):
    print('Dados de vendas inválidos')
else:
    lc= float(input('Lucro por unidade de coxinha: R$ '))
    lq= float(input('Lucro por unidade de quibe: R$ '))
    lucro= calculaLucros(cox, qui, lc, lq)
    print(f'Lucros: {lucro}')
    maior= -math.inf
    menor= math.inf
    for i in range(len(lucro)):
        if lucro[i]> maior:
            maior=lucro[i]
        if lucro[i] < menor:
            menor = lucro[i]
    print(f'Maior lucro: R$ {maior:.2f}')
    print(f'Menor lucro: R$ {menor:.2f}')