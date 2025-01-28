somaidade = 0 
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0

for i in range(1,5):
  print(f'---------- {i}º PESSOA ----------')
  nome = str(input('Nome: ')).strip().upper()
  idade = int(input('Idade: '))
  somaidade += idade
  sexo = str(input('Sexo [M/F]: ')).strip()

  if i == 1 and sexo in 'Mm':
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Mm' and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Ff' and idade < 20:
    mulher20 += 1

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')