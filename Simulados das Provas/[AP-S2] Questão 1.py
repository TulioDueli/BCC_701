from biblioteca import*
import math

def calculosVetor(x):
    menor = math.inf
    maior = -math.inf
    media = 0
    ele = len(x)
    for i in range(len(x)):
        if x[i] < menor:
            menor = x[i]
        if x[i] > maior:
            maior = x[i]
        media += x[i]
    return ele, round(menor, 2), round(maior, 2), round(media/len(x), 2)

print('Manipulações de valores de Vetor')
x = inputVetor('Vetor X: ', float)
print('Propriedades do vetor X:')
el, men, mai, med = calculosVetor(x)
print(f'. Possui {el} elementos')
print(f'. {men:.2f} é o menor valor')
print(f'. {mai:.2f} é o maior valor')
print(f'. A média dos valores é {med:.2f}')