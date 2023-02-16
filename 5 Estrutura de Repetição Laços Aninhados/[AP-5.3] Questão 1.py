r= input('Deseja imprimir um retângulo? (s/n) ')
ast= '*'
while r=='s':
    a= int(input('\nAltura do retângulo: '))
    l= int(input('Largura do retângulo: '))
    while (a<=0 or a>l) or (l<=0 or l<a):
        print('Entrada inválida.')
        a= int(input('\nAltura do retângulo: '))
        l= int(input('Largura do retângulo: '))
    print()
    for i in range(a):
        for t in range(l):
            print(f'{ast}', end='')
        print()
    r= input('\nDeseja imprimir outro retângulo? (s/n) ')
