n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print (f'calculando {n}! =', end=' ')
while c > 0:
    print(f'{c} ', end= ' ' )
    print(' x ' if c> 1 else ' = ', end=' ')
    f *= c #fatorial
    c -= 1   #vai decrescendo
print(f'{f}')