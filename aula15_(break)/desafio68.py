from random import randint

vitorias = 0

while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0 , 10)
    total = jogador + computador
    tipo = ' '
     
      # Escolha do jogador (Par ou Ímpar)
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')

    if total % 2 == 0:
       print('DEU PAR')
    else:
        print('DEU IMPAR')

    if (total % 2 == 0 and tipo == 'P') or (total % 2 == 1 and tipo == 'I'):
            print('PARABENS VOCÊ VENCEU')
            print('Vamos jogar novamente')
            vitorias+=1
    else:
            print(' Você PERDEU!')
            break
print(f'Você venceu com {vitorias} vitórias consecutivas')