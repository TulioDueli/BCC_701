a1 = float(input('Informe o primeiro termo:'))
q = float(input('Informe a razão:'))
n = int(input('Informe o número do termo:'))
n1 = n - 1
an = a1 * q**n1
print(f'O termo a({n}) é {an: .2f}')