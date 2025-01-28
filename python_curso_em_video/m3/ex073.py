times = (
    "Botafogo", "Palmeiras","Flamengo","Fortaleza", "Internacional", "São Paulo","Corinthians","Bahia","Cruzeiro","Vasco da Gama","Vitória",
    "Atlético Mineiro","Fluminense","Grêmio","Red Bull Bragantino","Juventude","Athletico Paranaense","Criciúma","Atlético Goianiense","Cuiabá"
)
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)

print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Fluminense está na {times.index('Fluminense')+1}° posição')


