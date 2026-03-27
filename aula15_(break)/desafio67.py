
while True:
    num = int(input('Digite um numero para a sua tabuada (-1 para sair do loop): '))

    if num == -1:
        print('Encerrado')
        break
    i = 1
    while i <= 10:
        print(f'{num} x {i} = {num * i}')
        i+=1
    print("-" * 20)
