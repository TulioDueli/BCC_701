from bib import*
def getDivisores(x):
    v=[]
    for j in range(1, x+1):
        n= x%j  # % é equivalente ao resto da divisão, ent se o resto é zero, o número é divisível pelo outro
        if n==0:
            v.append(j)
    return(v)

num= inputVetor('Digite os números: ', int)
if len(num)==0:
    print('\nNenhum número informado')
else:
    for i in range(len(num)):
        div= getDivisores(num[i])
        if len(div)==2:
            print(f'\n{num[i]} é um número primo.')
        else:
            print(f'\n{num[i]} não é um número primo.')
            print('Seus divisores são:')
            print(f'{div}')