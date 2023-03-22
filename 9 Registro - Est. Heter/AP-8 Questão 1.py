import math

def calculaComprimento(reta):
    c = math.sqrt((reta["B"]["X"]-reta["A"]["X"])**2 + ((reta["B"]["Y"]-reta["A"]["Y"]))**2)
    return round(c, 2)
   
A = {
    "X": float(input('- Coordenada X de A: ')),
    "Y": float(input('- Coordenada Y de A: '))  
}

B = {
    "X": float(input('- Coordenada X de B: ')),
    "Y": float(input('- Coordenada Y de B: '))  
}

reta = {}
reta["A"] = A
reta["B"] = B

cal = calculaComprimento(reta)
print(f'\nDistância entre os pontos A e B: {cal:.2f}')