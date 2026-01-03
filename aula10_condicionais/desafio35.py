print('-=-'*20)
print('Analisador de triangulo')
print('-=-'*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento: '))
r3 = float(input('terceiro segmento:'))
if r1< r2 + r3 and r2 < r1 +r3 and r3< r1 +r2:
    print('Os segmentos acima Podem Formar triangulo! ')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulos')
    