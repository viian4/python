peso = float(input('Qual seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura**2)

print(f"Seu IMC é: {imc:.2f}")
#classificação
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:#entre 18.5 e 25
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 35:
    print("Classificação: Obesidade grau I")
elif 35 <= imc < 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III (mórbida)")