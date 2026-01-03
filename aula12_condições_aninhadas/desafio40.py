nota1= float(input('primeira nota: '))
nota2= float(input('Segunda nota:  '))
media = (nota1 + nota2 )/2
print (f'a nota entre {nota1:.2f} e {nota2:.2f} é igual a {media:.2f}')
if media < 5.0: # ou if 7 > media >= 5
    print('REPROVADO')
elif media <= 6.9:
    print('RECUPERAÇAO')
elif media >= 7.0:
    print('APROVADO') # ou else : print (Aprovado)
    