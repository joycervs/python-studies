soma = 0
cont = 0

for i in range(1, 501, 2):
  if i % 3 == 0:
    soma += i
    cont += i
print(f'A soma de todos os {cont} valores solicitados é {soma}')
