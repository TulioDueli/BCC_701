def Relatorio(funs, C):
    ST = 0
    TH = 0
    for i in range(len(funs)):
        if C == (funs[i]["Cargo"]):
            ST += funs[i]["Salário"]
            TH += funs[i]["Horas"]
    return round(ST, 3), TH

f = int(input('Informe a quantidade de funcionários: '))

print('\nEntrada dos funcionários:')

funs = []
for i in range(f):
    fun = {}
    print(f'\nFuncionário {i+1}')
    fun["Cargo"] = input('. Informe o Cargo: ')
    fun["Salário"] = float(input('. Informe o Salário: R$ '))
    fun["Horas"] = int(input('. Informe as Horas: '))
    funs.append(fun)

print('\nRelatórios:')

C = 'c'
while C != '':
    C = input('\nInforme o Cargo: ')
    st, th = Relatorio(funs, C)
    if C != '':
        print(f'. Salário Total: R${st:.2f}')
        print(f'. Total de horas: {th}')
