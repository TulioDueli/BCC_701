from biblioteca import*
import math
notas= inputMatriz('Matriz de notas: ', float)

maior= -math.inf
menor= math.inf

for i in range(len(notas)):
    for t in range(len(notas[i])):
        if notas[i][t]>maior:
            maior=notas[i][t]
        if notas[i][t]<menor:
            menor=notas[i][t]
            
            
print(f'\nMenor nota: {menor}')
print('Alunos com a menor nota:')
for i in range(len(notas)):
    for t in range(len(notas[i])):
        if notas[i][t]==menor:
            print(f'. {i}')
            
print(f'\nMenor nota: {maior}')
print('Alunos com a maior nota:')
for i in range(len(notas)):
    for t in range(len(notas[i])):
        if notas[i][t]==maior:
            print(f'. {i}') 