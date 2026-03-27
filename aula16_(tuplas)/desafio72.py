'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

vinte = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')

while True:
    x = int(input('Digite um numero de 0 a 20: '))
    if 0 <= x <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {vinte[x]}.')