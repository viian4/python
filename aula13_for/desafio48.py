soma = 0 #acumulador
cont = 0
for c in range (1, 501, 2):
    if c % 3== 0:
       cont = cont + 1
       soma = soma + c 
print(f'A soma de todos os valores {cont} solicidados é {soma}')

#estudar mais esse
