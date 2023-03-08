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

def acimaMedia(notas,md):
    a=[]
    for i in range(len(notas)):
        if notas[i]>md:
            a.append(i)
    return a

notas= inputVetor('Notas: ', float)
ma, mn, md= estatNotas(notas)
print(f'Maior nota: {ma}\nMenor nota: {mn}\nNota média: {md}')
print('Notas acima da média:')
aci= acimaMedia(notas,md)
for i in range(len(aci)):
    print(f'  - [{aci[i]}] = {notas[aci[i]]:.1f}')