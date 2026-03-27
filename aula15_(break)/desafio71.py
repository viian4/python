'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
valor = int(input("Digite o valor que deseja sacar:"))

notas = [200, 100, 50, 20, 10, 5, 2]

for nota in notas:
    quantidade = valor // nota
    print(f"{quantidade} de notas de R${nota}") 
    valor = valor % nota