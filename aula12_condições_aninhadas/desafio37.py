numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão:
[ 1 ] converter para BÍNARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{numero} convertido para BINARIO è igual a {bin(numero)[2:]}')
elif opção == 2:
    print(f'{numero} convertido para OCTAL è igual a {oct(numero)[2:]}')
elif opção == 3:
    print(f'{numero} convertido para OCTAL è igual a {hex(numero)[2:]}')
else:
    print('Opção invalida')