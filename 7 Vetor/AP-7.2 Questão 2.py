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
def acimaMedia(n,med):
    a=[]
    for i in range(len(n)):
        if n[i]>med:
            a.append(i)
    return a
n= inputVetor('Notas: ', float)
ma, me, med= estatNotas(n)
print(f'Maior nota: {ma}\nMenor nota: {me}\nNota média: {med}')
print('Notas acima da média:')
aci= acimaMedia(n,med)
for i in range(len(aci)):
    print(f'  - [{aci[i]}] = {n[aci[i]]:.1f}')