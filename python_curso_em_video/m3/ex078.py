listanum = []
maior = menor = 0

for n in range(0,5):
  listanum.append(int(input(f'Digite um valor na posição {n}: ')))

  if n == 0:
    maior = menor = listanum[n]
  else:
    if listanum[n] > maior:
      maior = listanum[n]
    if listanum[n] < menor:
      menor = listanum[n]

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
  if v == maior:
    print(f'{i}... ', end='')
print()


print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
  if v == menor:
    print(f'{i}... ', end='')
print()