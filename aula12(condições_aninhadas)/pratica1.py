nome = str(input('Qual o seu nome:'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome =='Paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino.')
else:
    print(f'Tenha um bom dia, {nome}')