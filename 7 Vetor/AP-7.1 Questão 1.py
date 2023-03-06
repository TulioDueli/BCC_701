from biblioteca import*
c= inputVetor('Digite os nomes dos candidatos: ', str)
v= inputVetor('Digite as quantidades de votos: ', int)
if len(v)!=len(c):
    print('Vetores com tamanhos diferentes')
elif len(c)<3:
    print('Quantidade de candidatos insuficiente')
else:
    maior= 0
    for i in range(len(v)):
        if v[i]> maior:
            maior=v[i]
            indice = i
    print(f'Vencedor das eleições: {c[indice]}')
        
        
