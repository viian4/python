# Quantos termos você quer mostrar
n = int(input("Quantos termos da sequência Fibonacci você quer ver? "))

t1 = 0   # primeiro termo
t2 = 1   # segundo termo
cont = 0 # contador para controlar o while

print("Sequência de Fibonacci:")
while cont < n:
    print(t1, end=" ")  # mostra o termo atual
    t3 = t1 + t2        # próximo termo é a soma dos dois anteriores
    t1 = t2             # atualiza: o segundo passa a ser o primeiro
    t2 = t3             # o terceiro passa a ser o segundo
    cont += 1           # soma +1 ao contador
