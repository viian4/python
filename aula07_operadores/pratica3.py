n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2
print('A soma e {}, o produto é {} e a divisao é {:.3f}'.format(s, m, d) )
#end='' => nao quebra a linha 
#\n => quebrar linha
print ('A divisão intera {} e potencia {}'.format(di, e))