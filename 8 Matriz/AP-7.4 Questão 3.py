from biblioteca import*

pri = inputMatriz('Informe os resultados do atleta 1: ', int)
seg = inputMatriz('Informe os resultados do atleta 2: ', int)
qlin1, qcol1 = dimMatriz(pri)
qlin2, qcol2 = dimMatriz(seg)

if qlin1!=qlin2 or qcol1!=qcol2:
    print('Matrizes incompatíveis.')

else:
    vit1 = 0
    vit2 = 0
    emp = 0
    for i in range(len(pri)):
        for t in range(len(pri[i])):
            if pri[i][t]>seg[i][t]:
                vit1+=1
            elif seg[i][t]>pri[i][t]:
                vit2+=1
            else:
                emp+=1
    print(f'Quantidade de vitórias do atleta 1: {vit1}')
    print(f'Quantidade de vitórias do atleta 2: {vit2}')
    print(f'Quantidade de empates: {emp}')