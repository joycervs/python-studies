soma = quant = media = maior = menor = 0
resp = 'S'

while resp in 'Ss':
  n = int(input('Digite um número: '))
  soma += n
  quant += 1
  if quant == 1:
    maior = menor = n
  else:
    if n > maior: 
      maior = n
    if n < menor:
      menor = n
  resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')