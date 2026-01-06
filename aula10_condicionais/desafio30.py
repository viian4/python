numero = int(input('Me diga um número qualquer:'))
resultado = numero % 2 # resto da divisao por 2
print(f'O resultado foi {resultado}')
if resultado == 0: #se o resto for 0 o número é par
    print(f'O numero {numero} é PAR')
else:
    print(f'O numero {numero} é IMPAR')