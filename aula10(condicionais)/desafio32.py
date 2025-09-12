from datetime import date
ano = int(input('Qual ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 400 == 0:
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÂO é BISSEXTO. ')
