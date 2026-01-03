r1 = float(input('Primeiro segment: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FPRMAR triangulo')
    if r1 == r2  == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulos')