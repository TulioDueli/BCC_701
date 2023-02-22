import math
def converteMedidas(a):
    FT= a*0.3048
    YD= a*0.9144
    return round(FT, 3), round(YD, 3)
p= int(input('Quantidade de percursos: '))
for i in range(1, p+1):
    print(f'Percurso {i}: ')
    M= float(input('- Tamanho em metros: '))
    ft, yd= converteMedidas(M)
    print(f' - Tamanho em pés...:{ft:.2f}')
    print(f' - Tamanho em jardas:{yd:.2f}')
    
    