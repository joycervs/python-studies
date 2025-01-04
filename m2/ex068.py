from random import randint

print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)

v = 0

while True:
  jogador = int(input('Diga um valor: '))
  computador = randint(0, 10)
  total =  jogador + computador
  opcao = ' '
  while opcao not in 'PI':
    opcao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
  print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')

  if opcao == 'P':
      if total % 2 == 0:
        print('Você VENCEU!')
        v += 1
      else:
        print('Você PERDEU!')
        break
  elif opcao == 'I': 
    if total % 2 == 1:
      print('Você VENCEU!')
      v += 1
    else:
      print('Você PERDEU!')
      break
  print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
