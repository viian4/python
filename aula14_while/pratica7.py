import time

contador = int(input('Tempo:'))

while contador >= 0:
    print(contador)
    time.sleep(1)
    contador -= 1
print('fim')