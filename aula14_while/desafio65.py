resp = 'S'
soma = cont = num = maior = menor =0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num #soma o número
    cont += 1 #continua rodando o programa até dizer a resposta ser 'não'
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')) .upper() .strip()
media = soma/cont
print (f'a soma dos números é igual a {soma}')
print (f'A média é igual a {media}')