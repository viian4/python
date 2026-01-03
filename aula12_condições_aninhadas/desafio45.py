from random import randint
from time import sleep
item =('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
# print(f'O computador escolheu {item[computador]}')
print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOO!!')
print('-='* 11)
print(f'Computador jogou {item[computador]}')
print(f'Jogador jogou {item[jogador]}')
print('-='* 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador ==2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
