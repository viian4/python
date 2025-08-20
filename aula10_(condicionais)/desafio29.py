velocidade = float(input('Qual a velocidae do carro? ')) 
if velocidade > 80:
    print('MULTADO! você excedeu o limite permitido (80km/h)')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança! ')
