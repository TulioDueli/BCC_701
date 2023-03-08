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

notas= inputVetor('Notas: ', float)
ma, mn, md= estatNotas(notas)
print(f'Maior nota: {ma}')
print(f'Menor nota: {mn}')
print(f'Nota média: {md}')