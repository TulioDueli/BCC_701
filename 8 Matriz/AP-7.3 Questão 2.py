from biblioteca import*

m= inputMatriz('Digite os elementos da matriz: ', int)
qlin, qcol= dimMatriz(m)

if qlin!=qcol:
    print('\nA matriz não é quadrada.')
    
else:
    print('\nElementos da diagonal principal:')
    for i in range(len(m)):
        print(f'{m[i][i]}', end='' )
        if i<len(m)-1:
            print(', ', end='')
#   for i in range(len(m)-1):
#       print(f'{m[i][i]},', end='')
#   for i in range(len(m)-1, len(m)):
#       print(f'{m[i][i]}')
#   ^^^^^ Outra forma de fazer ^^^^^
