#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = (str(input('Informe seu sexo: ')))
while sexo not in 'mMfF':
    sexo =(str(input('Dados invalidos. Informe seu sexo: '))) .strip() .upper()
print(f'sexo {sexo} registrado com sucesso.')