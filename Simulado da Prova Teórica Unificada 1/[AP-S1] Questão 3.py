a= int(input('Defina a quantidade de apresentações: '))
j= int(input('Defina a quantidade de juízes: '))
for i in range(1, a+1):
    print(f'. Apresentação {i}: ')
    d= float(input('. Grau de dificuldade: '))
    s=0
    for t in range(1, j+1):
        n= float(input(f'. Nota do juíz {t}: '))
        s+=n
    s*=d
    print(f'. Pontuação da apresentação: {s:.2f}')





