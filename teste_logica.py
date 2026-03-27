''' atividades de logica:
soma = 0
for i in range(5):
    numero =int(input("digite um numero: "))
    soma += numero
print(f"a soma dos números é {soma}")'''

'''numero = int(input('numero: '))
for i in range (1,11):
   print(f"{numero} X {i} = {numero * i}")'''

'''for conta in range(10,0,-1):
    print(conta)'''

'''palavra = str(input('Digeite uma palavra: '))

contador = 0
vogais = 'AEIOUaeiou'

for letra in palavra:
    if letra in vogais:
        contador += 1
print(f"A palavra '{palavra}' tem {contador} vogais.")'''

'''from random import randint
computador = randint(0,10)
palpite = 0
acertou = False

while not acertou:
    jogador = int(input('digite um numero: '))
    if jogador == computador:
        acertou = True
    else:
        print('tente novamente em outro momento:')
print('Parabens')'''

'''nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) /3
if media >= 7:
    print('APROVADO')
elif media >= 5:
    print('Recuperação')
elif media < 5:
    print("recuperação")

print(f"sua nota foi {media}")'''

'''for i in range(1,20,2): #começa do 1 ate 20 pulando de 2 em 2
   print(i)'''

'''palavra = str(input('digite uma palavra: '))
invertida = palavra[::-1]
print(invertida) '''


'''numero = int(input('digite um numero: '))
maior = 0
for i in range(4):
    maior = int(input('digite um numero: '))
    if numero > maior:
     maior = numero 
print(f'{maior}')'''

'''numero = int(input('digite um numero:'))
if numero % 2 == 0:
    print(f'{numero} é par')
else:
    print (f'{numero} é impar')'''

'''soma = 0
for i in range(10):
    numero = int(input('digite um numero: '))
    soma+=numero
print(f'A soma dos numeros é{soma}')'''
