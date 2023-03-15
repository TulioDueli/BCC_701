from biblioteca import*

print('Ministério do Meio Ambiente')
met = inputVetor('Metas dos estados: ', int)
arv = inputMatriz('plantio de árvores: ', int)
qlin, qcol = dimMatriz(arv)
for i in range(qcol):
    soma = 0
    for t in range(qlin):
        soma += arv[t][i]
    if soma<met[i]:
        print(f'Estado {i+1}, meta = {met[i]}, plantio = {soma}')