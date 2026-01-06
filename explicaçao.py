soma = 0 #Vai guardar o total acumulado.
numero = 1 #Será o contador que vai de 1 até 5
while numero <= 5:
    soma += numero # soma = soma + numero
    numero += 1  # aumenta o numero em +1 a cada repetição
print('soma total', soma)

'''Iteração 1 → soma = 0 + 1 = 1
   Iteração 2 → soma = 1 + 2 = 3
   Iteração 3 → soma = 3 + 3 = 6
   Iteração 4 → soma = 6 + 4 = 10
   Iteração 5 → soma = 10 + 5 = 15'''