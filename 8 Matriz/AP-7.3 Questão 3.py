from biblioteca import*
import math
m= inputMatriz('Digite os elementos da matriz: ', int)
qlin, qcol= dimMatriz(m)
identidade=0
for i in range(qlin):
    for t in range(qcol):
        if i==t:
            if m[i][t]==1:
                identidade+=1
        elif i<t:
            if m[i][t]==0:
                identidade+=1
        elif i>t:
            if m[i][t]==0:
                identidade+=1         
if identidade == qlin*qcol:
    print(f'A matriz é identidade.')
else:
    print('A matriz não é identidade.')

    