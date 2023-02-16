a = int(input('Cateto 1 (a):'))
b = int(input('Cateto 2 (b):'))
c = int(input('Hipotenusa (c):'))

if a**2 + b**2 == c**2:
    print(f'{a}, {b}, {c} representam um terno pitagórico')
else:
    print(f'{a}, {b}, {c} NÃO representam um terno pitagórico')