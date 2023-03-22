def Situacao(x):
    if x["nota"]>=6:
        s = 'APROVADO'
    elif x["nota"]<6 and x["nota"]>=3:
        s = 'EXAME ESPECIAL'
    else:
        s = 'REPROVADO'
    return s
    
a = int(input('Digite a quantidade de alunos: '))
alunos = []
for i in range(1, a+1):
    aluno = {}
    aluno["nome"] = input(f'\nNome do aluno {i}: ')
    aluno["nota"] = float(input(f'Nota do aluno {i}: '))
    alunos.append(aluno)
print('\nSituação dos alunos:')   
for i in range(len(alunos)):
    sit = Situacao(alunos[i])
    print(f'{i+1} {alunos[i]["nome"]} - Nota: {alunos[i]["nota"]:.2f} - {sit}')