P = float(input('Digite seu peso(em kg): '))
A = float(input('Digite sua altura(em metros): '))
Q = float(input('Digite a circunferência do seu quadril(em cm): '))
IMC = P / A**2
IAC = (Q / A**1.5) - 18
print(f'IMC= {IMC: .3f}')
print(f'IAC= {IAC: .3f}')