somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
'''somaidade: vai somar todas as idades para calcular a média.
   maioridadehomem: guarda a maior idade entre os homens (começa em 0).
   nomevelho: guarda o nome do homem mais velho (começa vazio).
    totmulher20: contador de mulheres com menos de 20 anos.'''
for p in range(1,5):
    print(f'_____{p} PESSOA_____')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    '''Soma a idade atual à somaidade (equivalente a somaidade = somaidade + idade).'''
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff'and idade < 20:
        totmulher20 += 1
mediaidade = somaidade /4
print(f'A soma da idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f' Ao todo são {totmulher20} mulheres com menos de 20 anos')
