n= input('Informe o nome do juiz: ')
p= int(input('Quantidade de partidas: '))
imp=0
fal=0
car=0
acr=0

for i in range(1, p+1):
    print(f'\nPartida {i}')
    imp+=int(input('. Impedimentos.......: '))
    fal+=int(input('. Faltas.............: '))
    car+=int(input('. Cartões............: '))
    acr+=float(input('. Tempo de acréscimo.: '))
print(f'\nEstatísticas do juiz {n}:')
print(f'. Impedimentos.......: {imp/p:.2f}.')
print(f'. Faltas.............: {fal/p:.2f}.')
print(f'. Cartões............: {car/p:.2f}.')
print(f'. Tempo de acréscimo.: {acr/p:.2f}.')