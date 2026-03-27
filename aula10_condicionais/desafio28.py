from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "pensar"
print('-=-' * 20 )
print('vou pensar em um numero entre 0 e 5, Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS!voce conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no numero {computador} e não numero {jogador}')


