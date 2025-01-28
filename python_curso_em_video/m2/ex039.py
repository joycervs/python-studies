from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
opcao = str(input('Digite o seu gênero(F/M): ')).strip().upper()
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

if opcao == 'F':
  print('O alistamento militar não é obrigatório para mulheres.')
elif opcao == 'M':
  if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
  elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    print(f'Seu alistamento será em {ano}.')
  elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano}.')
else:
  print('Entrada de gênero inválida. Digite "F" para feminino ou "M" para masculino.')

