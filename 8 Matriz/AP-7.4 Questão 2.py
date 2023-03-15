from biblioteca import*
import math

maior = -math.inf

pro = inputVetor('Informe os nomes dos produtos: ', str)
ven = inputMatriz('Informe as quantidades de vendas: ', int)

for i in range(len(ven)):
    soma = 0
    for t in range(len(ven[i])):
        soma += ven[i][t]
    if soma>maior:
        maior = soma
        indice = i

print(f'Produto selecionado: {pro[indice]}')
print(f'Total de vendas de {pro[indice]}: {maior}')
        

    