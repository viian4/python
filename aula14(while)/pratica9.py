soma = 0
contador = 0
while True:
    nota = float((input('Digite sua nota ( -1 para parar)')))

    if nota == -1:
        break

    soma += nota
    contador+=1

if contador > 0:
    media = soma / contador
    print(f'A media foi {media: .2f}')
else:
    print('nenhuma nota foi inserida')