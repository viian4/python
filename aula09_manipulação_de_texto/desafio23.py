num = int(input('Informe um numero: '))
U = num // 1 % 10
D= num // 10 % 10
C = num // 100 % 10
M = num // 1000 % 10
print(f'Analisando o numero {num} ')
print(f'Unidade {U}')
print(f'Dezena {D}')
print(f'Centena {C}')
print(f'Milhar {M}')