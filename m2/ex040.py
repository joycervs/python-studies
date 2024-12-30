nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print(f'A média do aluno é {media}')

if media > 7.0:
  print('Parabéns, você foi APROVADO!')
elif media >= 5 and media < 7:
  print('Você está de RECUPERAÇÃO!')
else: 
  print('Você foi REPROVADO!')