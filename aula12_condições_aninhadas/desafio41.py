from datetime import date
atual = date.today().year
nasc =int(input('Ano de nascimento: '))
idade = atual  - nasc
print(f' O atleta tem {idade} anos')
if idade <= 9:
    print('MIRIN')
elif idade <= 14:
    print('INfANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
elif idade > 25:
    print('MASTER')