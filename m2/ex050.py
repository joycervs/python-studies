soma = 0
cont = 0

for i in range(1, 7):
  n = int(input(f'Digite o {i}º número: '))
  if n % 2 == 0:
    soma += n 
    cont += 1
print(f'Você informou {cont} números pares e a soma deles é {soma}')
  