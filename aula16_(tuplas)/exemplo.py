'''lanche = ('Hamburguer', 'suco', 'pizza', 'pudim' )
#tupla sao imutaveis
print(lanche[1])'''

lanche = ('Hamburguer', 'suco' , 'pizza', 'pudim')
#for cont in range(len(lanche)):
    #print(f'eu vou comer {lanche[cont]} na posicao {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
     
#print(len(0, lanche))
#for comida in lanche:
    #print(f'Eu vou comer {comida}')
print('comi pra caramba')

#print(sorted(lanche)) => ordena  a tupla
# len => mostra o tamanho ou posicao
#c.count
#c.index