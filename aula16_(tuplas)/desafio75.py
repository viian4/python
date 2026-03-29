'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

# Lê 4 vezes e transforma o resultado final em tupla
numeros = tuple(int(input(f"Digite o {i+1}º valor: ")) for i in range(4))

print(f"\nOs números na tupla são: {numeros}")

#A) Quantas vezes apareceu o valor 9.
quantidade = numeros.count(9)
print(F"O numero 9 aparece {quantidade} veze(s)")

#B) Em que posição foi digitado o primeiro valor 3.
if 3 in numeros:
    posicao = numeros.index(3)
    print(f"O primeiro valor 3 foi digitado na {posicao + 1} posição (índice {posicao}).")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")

#C) Quais foram os números pares.
for n in numeros:
    if n % 2 == 0:
        print(f"{n} é par")
    else:
        print(f"{n} é ímpar")
   
