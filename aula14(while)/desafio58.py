#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
computador = randint(0, 10) #faz o computador "pensar"
print('-=-' * 20 )
print('vou pensar em um numero entre 0 e 10, Tente adivinhar...')
print('-=-' * 20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente')
        elif jogador > computador:
            print('Menos... tente novamente')
print (f"acertou com {palpite} tentativas")

