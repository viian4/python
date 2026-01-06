valor_casa = float(input("Qual o valor da casa?"))
salario = float(input('Qual o seu salario? '))
anos = float(input('Em quantos anos pretende pagar? '))
 #regra
parcela = valor_casa /(anos * 12)
limite = salario * 0.30
print(f'Valor da casa R${valor_casa:.2f}')
print(f'Salario R${salario:.2f}')
print(f'Anos {anos}')
print(f'Prestação R${parcela}')
print(f'30% do salario {limite}')
if parcela  <= limite:
    print('APROVADO')
else:
    print('NEGADO')
