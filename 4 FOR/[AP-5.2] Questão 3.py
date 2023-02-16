n1= input('Nome do candidato 1: ')
c1= int(input('Número do candidato 1: '))
n2= input('Nome do candidato 2: ')
c2= int(input('Número do candidato 2: '))
e= int(input('Quantidade de eleitores: '))
while e<3:
    print('A quantidade de eleitores é inferior a 3')
    e= int(input(f'Quantidade de eleitores: '))
vval=0; vinv=0; cn1=0; cn2=0
print('\n## Votação Iniciada')
for i in range(e):
    v= int(input('Número do candidato que deseja votar: '))
    if v==c1 or v==c2:
        vval+=1
    elif v!=c1 and v!=c2:
        vinv+=1
    if v==c1:
        cn1+=1
    elif v==c2:
        cn2+=1
print('## Votação Encerrada')
vtc=vval
if vval==0:
    vtc+=1
x= (vval*100)/e; y= (vinv*100)/e; z= (cn1*100)/vtc; w= (cn2*100)/vtc
print(f'Votos válidos: {x:.2f}% ({vval} votos)')
print(f'Votos inválidos: {y:.2f}% ({vinv} votos)')
print(f'Votos para {n1}: {z:.2f}% ({cn1} votos)')
print(f'Votos para {n2}: {w:.2f}% ({cn2} votos)')