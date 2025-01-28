from random import randint
from time import sleep

n = randint(0, 5)

print('\033[0;36m-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[0;36m-=-\033[m' * 20)

num = int(input('\033[0;35mEm que número eu pensei? '))
print('PROCESSANDO...\033[m')
sleep(2)

if num == n: 
  print('\033[1;32mPARABÉNS, você conseguiu me vencer!\033[m')
else:
  print(f'\033[1;31mGANHEI! Eu pensei no número {n} e não no {num}!\033[m')