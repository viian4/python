from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Escolha uma das opções abaixo:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa ''')
    opcao = int(input('>>>>>>Qual é a sua opção? '))
    if opcao == 1 :
        soma = n1 + n2
        print(f' a soma de {n1} + {n2} é {soma} ')
    elif opcao == 2:
         produto = n1 * n2
         print(f'O resultado de {n1} x {n2} é {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print (f'Entre {n1} e {n2} o maior valoe é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
