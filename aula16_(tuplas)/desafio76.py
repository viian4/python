'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos = ('Lápis', 1.75,
'Borracha', 2,
'Caderno', 15.90,
'Estojo', 25,
'Transferidor', 4.20,
'Compasso', 9.99,
'Mochila', 120.32,
'Canetas', 22.30,
'Livro', 34.90 )
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end= '' )
    else:
        print(f'R$ {produtos[pos]:>7.2f}')
