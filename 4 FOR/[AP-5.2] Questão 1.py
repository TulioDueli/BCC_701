t= int(input('Número de termos: '))
r= int(input('Raio da esfera: '))
pi=0
for i in range(0,t):
    pi+=((-1)**i)*(4/(2*i+1))
v= (4/3)*pi*(r**3)
print(f'pi = {pi:.5f}.')
print(f'Volume da esfera = {v:.5f}.')