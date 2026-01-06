num = int(input('Digite um numero para a sua tabuada: '))
for c in range(1,11): #11 por que o python sempre "engole" um numero
    print(f'{num} x {c:2} = {num*c}')
