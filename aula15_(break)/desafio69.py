maiores_18 = 0
total_homens = 0
mulheres_menos_20 = 0

while True:
    print('-' * 20)
    print('CADASTRO DA PESSOA')
    print('-' * 20)

    idade = int(input("Digite sua idade: "))

    # Verifica o sexo com segurança
    sexo = ''
    while sexo not in ('M', 'F'):
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo == '':
            print('⚠️ Digite M para masculino ou F para feminino.')

    # Contagens
    if idade >= 18:
        maiores_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = input('Você deseja continuar? [S/N]: ').strip().upper()
        if continuar == '':
            print('⚠️ Digite S para sim ou N para não.')

    if continuar == 'N':
        break

print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {maiores_18}')
print(f'Ao todo temos {total_homens} homens cadastrados.')
print(f'E temos {mulheres_menos_20} mulheres com menos de 20 anos.')
print('-' * 30)
