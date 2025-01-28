valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
      break

print(f'Foram digitados {len(valores)} elementos.')

valores.sort(reverse=True)
print(f'Valores digitados em ordem decrescente {valores}')

if 5 in valores:
   print('O valor 5 faz parte da lista')
else:
   print('O valor 5 não foi encontrado na lista')
