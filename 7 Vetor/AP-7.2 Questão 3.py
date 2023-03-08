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

def exameEspecial(notas):
    ee=[]
    for i in range(len(notas)):
        if notas[i]>=3 and notas[i]<6:
            ee.append(i)
    return ee

notas= inputVetor('Notas: ', float)
nomes= inputVetor('Nomes: ', str)

ma, mn, md= estatNotas(notas)
print(f'Maior nota: {ma}\nMenor nota: {mn}\nNota média: {md}')
print('Notas acima da média:')

aci= acimaMedia(notas,md)
for i in range(len(aci)):
    print(f'  - [{aci[i]}] = {notas[aci[i]]:.1f} ({nomes[aci[i]]})')
print('Notas em Exame Especial:')

exa= exameEspecial(notas)
for i in range(len(exa)):
    print(f'  - [{exa[i]}] = {notas[exa[i]]:.1f} ({nomes[exa[i]]})')