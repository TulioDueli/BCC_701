def Somatorio(a):
    S=0
    for i in range(1, a+1):
        S+= 1/i
    return round(S, 5)
def Produtorio(x):
    P=1
    for t in range(1, x+1):
        P*= 2**(1/t)
    return round(P, 5)
N=int(input('Quantidade de termos (N): '))
while N>0:
    s= Somatorio(N)
    p= Produtorio(N)
    print(f'. O valor de S é {s:.3f}\n. O valor de P é {p:.3f}')
    N=int(input('Quantidade de termos (N): '))