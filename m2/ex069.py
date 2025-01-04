print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)

maior18 = totalH = mulher20 = 0

while True:
  idade = int(input('Idade: '))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

  if idade >= 18:
    maior18 += 1
  if sexo == 'M':
    totalH += 1
  if sexo == 'F' and idade < 20:
    mulher20 += 1 

  continua = ' '
  while continua not in 'SN':
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if continua == 'N':
    break

print(f'Total de pessoas com mais de 18 anos : {maior18}')
print(f'Ao todo temos {totalH} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')