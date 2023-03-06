from biblioteca import*
import math
def estatNotas(x):
    maior= -math.inf
    menor= math.inf
    media= 0
    for i in range(len(x)):
        if x[i]>maior:
            maior=x[i]
        if x[i]<menor:
            menor=x[i]
        media+=x[i]
    return round(maior, 1), round(menor, 1), round(media/len(x), 1)
n= inputVetor('Notas: ', float)
ma, me, med= estatNotas(n)
print(f'Maior nota: {ma}')
print(f'Menor nota: {me}')
print(f'Nota média: {med}')