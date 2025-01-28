print('-=' * 20)
print('Analisador de Triângulos v.2')
print('-=' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
  print('Os segmentos acima PODEM formar um triângulo', end=' ')
  if a == b == c:
    print('EQUILÁTERO')
  elif a != b != c != a:
    print('ESCALENO')
  else:
    print('ISÓSCELES')
else:
  print('Os segmentos acima NÃO PODEM formar um triângulo')