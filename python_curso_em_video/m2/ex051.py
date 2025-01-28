primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for i in range (primeiro, decimo + razao, razao):
  print(f'{i}', end=' → ')
print('Acabou')