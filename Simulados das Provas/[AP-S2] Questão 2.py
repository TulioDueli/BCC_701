from biblioteca import*

print('Loja da tia Maria')

est = inputMatriz('Matriz de estoque: ', int)
n = int(input('Número de atualizações: '))

for i in range(n):
    inloj = int(input('Índice da loja: '))
    inpro = int(input('Índice do produto: '))
    nov = int(input('Novo estoque: '))
    est[inloj][inpro] = nov
    for t in range(len(est)):
        print(f'{est[t]}')
    