'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''
times = 'Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo',\
        'Vasco da Gama','Chapecoense','Atlético-MG','Botafogo','Athletico-PR',\
        'Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória','Coritiba',\
        'Avai','Ponte Preta','Atlético-GO'
print('-='*40)
print(f'Lista de times do Brasileirão {times}')
print('-='*40)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*40)
print(f'Os 4 ultimos são {times[-4:]}')
print('-='*40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*40)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')