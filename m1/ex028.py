from random import randint
from time import sleep

n = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)

if num == n: 
  print('PARABÉNS, você conseguiu me vencer!')
else:
  print(f'GANHEI! Eu pensei no número {n} e não no {num}!')