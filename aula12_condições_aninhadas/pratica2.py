idade = int(input('Digite sua idade: '))
nome = str(input('Digite seu nome: '))
if idade < 18:
    print(f'{nome} tem {idade}, logo  é menor de idade ')
else:
    print(f'{nome} tem {idade}, logo é maior de idade ')