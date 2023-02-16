import math
ini= int(input('Valor inicial: '))
while ini<-150 or ini>50:
    ini= int(input('Valor inicial: '))
fin= int(input('Valor final: '))
while fin<=ini:
    fin= int(input('Valor final: '))
pas= int(input('Passo: '))
while pas<=0:
    pas= int(input('Passo: '))
print()
print('x \ y |', end='')
c=0
for x in range(ini, fin+1, pas):
    print(f'{x:10d}', end='')
    c+=1
print('\n-------', end='')
print('-'*(10*c))
for y in range(ini, fin+1, pas):
    print(f'{y:5d} |', end='')
    for x in range(ini, fin+1, pas):
        if y<=30:
            e= y**2+((2*x)-3)
        if y>30 and y<=60:
            e= math.sin(0.0175*y)*math.cos(0.0175*x)
        if y>60 and y<=90:
            e= 1/(y**-2)+x
        if y>90:
            e= 3.14
        print(f'{e:10.2f}', end='')
    print()