from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0

for i in range(1,8):
  nasc = int(input(f'Data de nascimento da {i}º pessoa: '))
  idade = atual - nasc
  if idade >= 21:
    totalmaior += 1
  else:
    totalmenor += 1

print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade e {totalmenor} pessoas menores de idade.')