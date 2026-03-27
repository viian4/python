n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print(f'A sua nota foi {m:.1f}')
if m >= 6.0:
    print('PARABÉNS VOCÊ PASSOU!')
else:
    print('VOCÊ REPROVOU! TENTE NOVAMENTE :()')