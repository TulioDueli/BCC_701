from biblioteca import*
matriz= inputMatriz('Digite os elementos da matriz: ', int)
col= int(input('\nDigite a coluna que será alterada: '))
while col>=len(matriz[0]) or col<0:
    col= int(input('Digite uma coluna válida: '))
print('Matriz alterada:')
for i in range(len(matriz)):
    subs= (matriz[i][col])*2
    matriz[i][col] = subs
    print(f'{matriz[i]}')
