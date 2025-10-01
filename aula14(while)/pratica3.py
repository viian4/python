n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: #não lê 0 como numero impar
        if n % 2 == 0: 
            par += 1
        else: impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares')

'''if n != 0:
Verifica se o número lido é diferente de 0. Se for 0, não entra na contagem; o while terminará na próxima checagem (ou imediatamente, porque a condição while n != 0 ficará falsa na próxima iteração)'''