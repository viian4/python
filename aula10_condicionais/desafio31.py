distancia = float(input('Qual é a distanciada viagem? '))
print(f'Voce esta preste a começar uma viagem de {distancia}km. ')
if distancia <= 200:
    preço= distancia * 0.50
else:
    preço = distancia * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')