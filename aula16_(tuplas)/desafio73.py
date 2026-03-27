'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time do Flamengo.'''

times = ("Atlético-MG", "Athletico-PR", "Bahia", "Botafogo", "Corinthians", "Coritiba", "Cruzeiro", "Flamengo","Fluminense", "Fortaleza", "Grêmio", "Internacional",  "Juventude", "Mirassol", "Palmeiras", "Santos", "São Paulo","Vasco da Gama", "Vitória" )

# A)
print(times[:5])

#B)

print(times[-4:])

# C)
print(sorted(times))

# D)
print(f'O Flamengo está na posição {times.index("Flamengo") + 1}')

'''for i, time in enumerate(times):
    if time == "Flamengo":
        print(f'O Flamengo está na posição {i + 1}')
        
        
Por que usamos +1?
Porque em Python a contagem começa do 0, mas na vida real começa do 1.'''