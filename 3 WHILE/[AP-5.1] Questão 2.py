n= int(input('Informe o número que deseja calcular o Fatorial: '))
while n<=0:
    n= int(input('Número inválido, defina outro: '))
x= 1
fat= 1
while x<=n:
    fat*=x
    x+=1
print(f'O Fatorial de {n} é: {fat}')







