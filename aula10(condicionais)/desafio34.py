print('*** CALCULAR SALÁRIO *****')
salario = float(input('Entre com o salário do coladorador: '))
nome = str(input('Entre com o nome do funcionário: ')).strip()
base = 1250.00
if salario <= base:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'O novo salário do colaborador {nome} é de R$ {novo:.2f}')