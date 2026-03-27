n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s+= n 
print(f'A soma vale {s}')
#O break interrope o loop sem somar a flag(999), assim fazendo as soma dos números principais