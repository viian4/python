from random import randint
from time import sleep
computador = randint(0, 10) #faz o computador "pensar"
print('-=-' * 20 )
print('vou pensar em um numero entre 0 e 10, Tente adivinhar...')
print('-=-' * 20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Em que numero pensei? ')) # jogador tenta adivinhar
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print(f'Acertou com {palpite} tentativas. Parabéns!')