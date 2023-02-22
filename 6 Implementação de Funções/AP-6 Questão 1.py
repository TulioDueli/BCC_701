import math
def impostoRenda(a):
    if a<=1500:
        D= 0
    elif a<=2500:
        D= 0.05*a
    elif a<=4500:
        D= 0.1*a
    elif a>4500:
        D= 0.2*a
    return round(D, 2)
        
B= float(input('Digite o salário bruto: '))
ir= impostoRenda(B)
INSS= B*0.1
FGTS= B*0.11

print(f'(-)IR: R$ {ir:.2f}')
print(f'(-)INSS: R$ {INSS:.2f}')
print(f'FGTS: R$ {FGTS:.2f}')
print(f'Total de descontos: R$ {ir+INSS:.2f}')
print(f'Salário Líquido: R$ {B-(ir+INSS):.2f}')