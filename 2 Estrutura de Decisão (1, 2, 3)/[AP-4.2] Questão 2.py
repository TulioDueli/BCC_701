x = float(input('Digite seu peso (em kg): '))
y = float(input('Digite sua altura (em metros): '))
z = input('Seu sexo é masculino (M) ou feminino (F)? ')
IMC = x / (y**2)
if z == 'M':
    if IMC >25:
        peso = 25 * (y**2)
        x1 = x - peso
        print(f'Você deve perder {x1: .2f}kg para ter IMC = 25')
    else:
        print('Você não precisa perder peso para ter IMC <= 25')
if z == 'F':
    if IMC >24:
        peso = 24 * (y**2)
        x1 = x - peso
        print(f'Você deve perder {x1: .2f}kg para ter IMC = 24')
    else:
        print('Você não precisa perder peso para ter IMC <= 24')
#elemento de lista:
if z not in ['F','M']:
    print('A entrada contém dados não reconhecidos')