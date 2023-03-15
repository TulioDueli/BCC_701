from biblioteca import*

def somaMatriz(pri, seg):
    qlin, qcol = dimMatriz(pri)
    m=criarMatriz(qlin,qcol , 0)
    for i in range(qlin):
        for t in range(qcol):
            m[i][t] = pri[i][t] + seg[i][t] 
    return m

pri = inputMatriz('Digite a primeira matriz: ', int)
seg = inputMatriz('Digite a segunda matriz: ', int)
qlin, qcol = dimMatriz(pri)

if len(pri)!=len(seg):
    print('\nNão é possível somar as matrizes')
    
else:
    print('\nMatriz resultante:')
    soma = somaMatriz(pri,seg)
    for i in range(qlin):
        print(f'{soma[i]}')