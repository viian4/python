total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: RS '))
    cont += 1
    total += preco
    
    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' ' 
    while resposta not in 'SN':
        resposta = str( input('Quer continuar? ')).strip(). upper()
    if resposta == 'N':
        break

print('{:-^40}'.format('FIM DE PROGRAMA'))
print(f'O total da compra é R$5 {total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')